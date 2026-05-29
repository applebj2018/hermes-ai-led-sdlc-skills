#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
approval.py — 阶段审批检查点系统
==================================
AI-led-dev-methodology 的核心机制：
人类输入 → AI生成 → AI审计 → 人类审批 → 下一阶段

每个阶段结束时生成审批清单，人工确认后才能进入下一阶段。
审批状态持久化到 checkpoint.json，支持断点续跑。
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any


class ApprovalStatus(str, Enum):
    PENDING = "pending"       # 待审批
    APPROVED = "approved"     # 已批准
    REJECTED = "rejected"     # 已拒绝（需修改后重新提交）
    SKIPPED = "skipped"       # 已跳过（仅用于开发调试）


@dataclass
class PhaseCheckpoint:
    """阶段检查点"""
    phase: str                          # 阶段名称
    description: str                    # 阶段描述
    status: str = ApprovalStatus.PENDING  # 审批状态
    artifacts: list[str] = field(default_factory=list)  # 产出文件清单
    audit_report: str = ""              # 审计报告摘要
    approved_by: str = ""               # 审批人
    approved_at: str = ""               # 审批时间
    comments: str = ""                  # 审批意见
    rejection_reason: str = ""          # 拒绝原因


@dataclass
class ApprovalManifest:
    """审批清单"""
    project_name: str = ""
    created_at: str = ""
    checkpoints: list[PhaseCheckpoint] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_name": self.project_name,
            "created_at": self.created_at,
            "checkpoints": [asdict(cp) for cp in self.checkpoints],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ApprovalManifest":
        checkpoints = [
            PhaseCheckpoint(**cp) for cp in data.get("checkpoints", [])
        ]
        return cls(
            project_name=data.get("project_name", ""),
            created_at=data.get("created_at", ""),
            checkpoints=checkpoints,
        )


class ApprovalManager:
    """审批管理器"""

    CHECKPOINT_FILE = "checkpoint.json"

    # 标准阶段定义
    PHASES = [
        PhaseCheckpoint(
            phase="Phase 0",
            description="项目初始化 — SOUL.md, AGENTS.md, 目录结构",
        ),
        PhaseCheckpoint(
            phase="Phase 1",
            description="需求分析 — INITIAL.md, 需求文档",
        ),
        PhaseCheckpoint(
            phase="Phase 2",
            description="架构设计 — ARCHITECTURE.md, DATA-MODEL.md",
        ),
        PhaseCheckpoint(
            phase="Phase 2.5",
            description="功能设计 — UI 设计, 权限模型, 原型",
        ),
        PhaseCheckpoint(
            phase="Phase 3-4",
            description="编码实施 — 源代码, 单元测试",
        ),
        PhaseCheckpoint(
            phase="Phase 5",
            description="测试工程 — 测试套件, 测试报告",
        ),
        PhaseCheckpoint(
            phase="Phase 6",
            description="文档同步 — 用户手册, 交付文档",
        ),
        PhaseCheckpoint(
            phase="Phase 7",
            description="质量审计 — pyright, pytest, 审计报告",
        ),
    ]

    def __init__(self, project_dir: str) -> None:
        self.project_dir = project_dir
        self.checkpoint_path = os.path.join(project_dir, self.CHECKPOINT_FILE)
        self.manifest = self._load_or_create()

    def _load_or_create(self) -> ApprovalManifest:
        """加载或创建审批清单"""
        if os.path.exists(self.checkpoint_path):
            with open(self.checkpoint_path, "r", encoding="utf-8") as f:
                return ApprovalManifest.from_dict(json.load(f))

        manifest = ApprovalManifest(
            project_name=os.path.basename(self.project_dir),
            created_at=datetime.now().isoformat(),
            checkpoints=self.PHASES,
        )
        self._save(manifest)
        return manifest

    def _save(self, manifest: ApprovalManifest | None = None) -> None:
        """保存审批清单"""
        manifest = manifest or self.manifest
        with open(self.checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(manifest.to_dict(), f, ensure_ascii=False, indent=2)

    def get_phase_status(self, phase: str) -> ApprovalStatus:
        """获取阶段审批状态"""
        for cp in self.manifest.checkpoints:
            if cp.phase == phase:
                return ApprovalStatus(cp.status)
        return ApprovalStatus.PENDING

    def is_approved(self, phase: str) -> bool:
        """检查阶段是否已批准"""
        return self.get_phase_status(phase) == ApprovalStatus.APPROVED

    def can_proceed(self, phase: str) -> bool:
        """
        检查是否可以进入下一阶段。
        要求：当前阶段已批准，或所有前置阶段已批准。
        """
        phase_order = [cp.phase for cp in self.manifest.checkpoints]
        if phase not in phase_order:
            return True

        current_idx = phase_order.index(phase)
        # 检查所有前置阶段
        for i in range(current_idx):
            prev_phase = phase_order[i]
            status = self.get_phase_status(prev_phase)
            if status not in (ApprovalStatus.APPROVED, ApprovalStatus.SKIPPED):
                return False
        return True

    def submit_phase(
        self,
        phase: str,
        artifacts: list[str] | None = None,
        audit_report: str = "",
    ) -> None:
        """
        提交阶段产出，等待审批。

        Args:
            phase: 阶段名称
            artifacts: 产出文件清单
            audit_report: 审计报告摘要
        """
        for cp in self.manifest.checkpoints:
            if cp.phase == phase:
                cp.status = ApprovalStatus.PENDING
                cp.artifacts = artifacts or []
                cp.audit_report = audit_report
                cp.approved_by = ""
                cp.approved_at = ""
                cp.comments = ""
                cp.rejection_reason = ""
                self._save()
                break

    def approve_phase(
        self,
        phase: str,
        approved_by: str = "user",
        comments: str = "",
    ) -> None:
        """批准阶段"""
        for cp in self.manifest.checkpoints:
            if cp.phase == phase:
                cp.status = ApprovalStatus.APPROVED
                cp.approved_by = approved_by
                cp.approved_at = datetime.now().isoformat()
                cp.comments = comments
                self._save()
                break

    def reject_phase(
        self,
        phase: str,
        approved_by: str = "user",
        rejection_reason: str = "",
    ) -> None:
        """拒绝阶段，需要修改后重新提交"""
        for cp in self.manifest.checkpoints:
            if cp.phase == phase:
                cp.status = ApprovalStatus.REJECTED
                cp.approved_by = approved_by
                cp.approved_at = datetime.now().isoformat()
                cp.rejection_reason = rejection_reason
                self._save()
                break

    def skip_phase(self, phase: str) -> None:
        """跳过阶段（仅用于开发调试）"""
        for cp in self.manifest.checkpoints:
            if cp.phase == phase:
                cp.status = ApprovalStatus.SKIPPED
                self._save()
                break

    def print_status(self) -> None:
        """打印审批状态"""
        print("\n" + "=" * 60)
        print(f"  项目审批状态: {self.manifest.project_name}")
        print("=" * 60)

        status_icons = {
            ApprovalStatus.PENDING: "⏳",
            ApprovalStatus.APPROVED: "✅",
            ApprovalStatus.REJECTED: "❌",
            ApprovalStatus.SKIPPED: "⏭️",
        }

        for cp in self.manifest.checkpoints:
            icon = status_icons.get(cp.status, "?")
            print(f"  {icon} {cp.phase:10s} | {cp.description}")

            if cp.status == ApprovalStatus.REJECTED and cp.rejection_reason:
                print(f"     拒绝原因: {cp.rejection_reason}")
            if cp.status == ApprovalStatus.APPROVED and cp.comments:
                print(f"     审批意见: {cp.comments}")

        print("=" * 60)

        # 统计
        approved = sum(
            1
            for cp in self.manifest.checkpoints
            if cp.status == ApprovalStatus.APPROVED
        )
        total = len(self.manifest.checkpoints)
        print(f"  进度: {approved}/{total} 阶段已批准")
        print()

    def interactive_approve(self) -> None:
        """交互式审批"""
        self.print_status()

        print("请选择要操作的项目:")
        print("  输入阶段编号 (1-8) 进行审批")
        print("  输入 'q' 退出")
        print()

        for i, cp in enumerate(self.manifest.checkpoints, 1):
            print(f"  {i}. {cp.phase} - {cp.description}")

        try:
            choice = input("\n请选择: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n取消操作")
            return

        if choice.lower() == "q":
            return

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(self.manifest.checkpoints):
                cp = self.manifest.checkpoints[idx]
                self._approve_phase_interactive(cp)
        except ValueError:
            print("无效输入")

    def _approve_phase_interactive(self, cp: PhaseCheckpoint) -> None:
        """交互式审批单个阶段"""
        print(f"\n审批: {cp.phase} - {cp.description}")
        print(f"  当前状态: {cp.status}")

        if cp.status == ApprovalStatus.APPROVED:
            print("  该阶段已批准")
            return

        print("\n请选择操作:")
        print("  1. 批准")
        print("  2. 拒绝")
        print("  3. 跳过 (仅调试)")
        print("  4. 取消")

        try:
            action = input("\n请选择 (1-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n取消操作")
            return

        if action == "1":
            comments = input("审批意见 (可选): ").strip()
            self.approve_phase(cp.phase, comments=comments)
            print(f"  ✅ {cp.phase} 已批准")
        elif action == "2":
            reason = input("拒绝原因: ").strip()
            self.reject_phase(cp.phase, rejection_reason=reason)
            print(f"  ❌ {cp.phase} 已拒绝: {reason}")
        elif action == "3":
            self.skip_phase(cp.phase)
            print(f"  ⏭️ {cp.phase} 已跳过")
        else:
            print("  取消操作")

        self._save()
        self.print_status()


def main() -> None:
    """CLI 入口"""
    import argparse

    parser = argparse.ArgumentParser(description="阶段审批检查点管理")
    parser.add_argument(
        "--dir",
        default=".",
        help="项目目录 (默认: 当前目录)",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="显示审批状态",
    )
    parser.add_argument(
        "--approve",
        help="批准指定阶段 (如: Phase 1)",
    )
    parser.add_argument(
        "--reject",
        help="拒绝指定阶段 (如: Phase 1)",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="交互式审批",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="重置所有审批状态",
    )

    args = parser.parse_args()
    manager = ApprovalManager(args.dir)

    if args.reset:
        manager.manifest = ApprovalManifest(
            project_name=os.path.basename(args.dir),
            created_at=datetime.now().isoformat(),
            checkpoints=ApprovalManager.PHASES,
        )
        manager._save()
        print("审批状态已重置")
        manager.print_status()
    elif args.status:
        manager.print_status()
    elif args.approve:
        manager.approve_phase(args.approve)
        print(f"✅ {args.approve} 已批准")
    elif args.reject:
        reason = input("拒绝原因: ").strip()
        manager.reject_phase(args.reject, rejection_reason=reason)
        print(f"❌ {args.reject} 已拒绝")
    elif args.interactive:
        manager.interactive_approve()
    else:
        manager.print_status()


if __name__ == "__main__":
    main()
