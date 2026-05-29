---
name: ai-led-dev-overview
description: "AI主导的软件全生命周期开发方法论总览。覆盖从环境配置到交付运维的完整流水线。"
version: 1.0.0
metadata:
  hermes:
    tags: [agentic-engineering, AI-led-development, SDLC, 软件全生命周期, 需求分析, 架构设计, 编码实施, 测试工程, 文档交付, 变更管理]
    related_skills: [ai-led-dev-project-init, ai-led-dev-requirements, ai-led-dev-architecture, ai-led-dev-feature-design, ai-led-dev-implementation, ai-led-dev-testing, ai-led-dev-documentation, ai-led-dev-change-mgmt, ai-led-dev-version-control, ai-led-dev-quality-audit, ai-led-dev-user-preference, ai-led-dev-domain-spec]
---

# AI主导的软件全生命周期开发方法论 — 总览

## 核心理念

**AI 作为主要执行者，人类作为决策者。**

方法论遵循严格流水线：`人类输入 → AI生成 → AI审计 → AI迭代 → 人类审批 → 下一阶段`。每个阶段的输出成为下一阶段的输入。人类的角色从执行者转变为监管者——提供初始输入、审查AI输出、做出最终决策。

## 阶段流转图

```
Phase 0:   项目初始化与Agent配置
  ├── 输出: SOUL.md, AGENTS.md, CLAUDE.md, 项目目录结构
  └── 移交 → Phase 1

Phase 1:   需求工程
  ├── 输出: INITIAL.md (项目规格说明书), 需求文档
  └── 移交 → Phase 2

Phase 2:   架构设计
  ├── 输出: ARCHITECTURE.md, DATA-MODEL.md, 技术选型决策
  └── 移交 → Phase 2.5

Phase 2.5: 功能设计
  ├── 输出: 权限设计, 工作流设计, UI组件清单, 设计令牌, HTML原型
  └── 移交 → Phase 3

Phase 3:   测试数据生成
  ├── 输出: test_data/ (正常/边界/异常/并发场景)
  └── 移交 → Phase 4

Phase 4:   编码实施
  ├── 输出: 源代码, 单元测试, 模块文档(每个模块对应.md)
  └── 移交 → Phase 5

Phase 5:   测试工程
  ├── 输出: 测试套件, TDAD映射, 测试报告, 覆盖率分析
  └── 移交 → Phase 6

Phase 6:   文档同步与交付
  ├── 输出: 交付指南, 用户手册, 变更日志
  └── 移交 → Phase 7

Phase 7:   变更管理与迭代
  ├── 输出: 变更分析报告, 更新的产物
  └── 移交 → 任意阶段(L1→代码, L2→代码+文档+测试, L3→完整循环)

Phase 8:   版本管理与发布
  ├── 输出: 发布说明, 补丁验证, 部署脚本
  └── 移交 → Phase 9

Phase 9:   团队协作
  └── 输出: 协作报告, 契约同步
```

## 双Agent架构

每个项目使用 **两个AI Agent**：

| Agent | 角色 | 职责 |
|-------|------|------|
| **生成Agent** | 百变角色 | 根据当前阶段扮演产品经理、架构师、开发、测试、DevOps等角色 |
| **审计Agent** | 质量关卡 | 审查生成Agent的输出，查找遗漏/错误/风险，输出结构化审计报告 |

**每个阶段的核心工作流：**
1. 人类提供输入（需求/设计/数据）
2. 生成Agent搜索业界最佳实践 → 生成初稿
3. 审计Agent审查初稿 → 输出审计报告
4. 生成Agent根据审计报告迭代修改
5. 人类审查最终结果 → 批准或要求修改
6. 批准后输出作为下一阶段的输入

## 三层契约体系

用于团队协作和AI一致性保障：

```
第一层: ARCHITECTURE.md  (架构契约) — 全团队共享
  - 系统边界、模块划分、接口协议
第二层: DESIGN.md        (设计契约) — 模块间共享
  - 函数签名、数据模型、算法描述
第三层: module.md        (实现契约) — 文件级共享
  - 核心逻辑、算法细节、测试方法
```

## 通用命名规范

| 标识符类型 | Python | JavaScript/TypeScript | SQL | 环境变量 |
|-----------|--------|----------------------|-----|---------|
| 变量/函数 | snake_case | camelCase | — | — |
| 类/接口 | PascalCase | PascalCase | — | — |
| 常量 | UPPER_SNAKE_CASE | UPPER_SNAKE_CASE | — | UPPER_SNAKE_CASE |
| 私有成员 | _前缀下划线 | _前缀驼峰 | — | — |
| 表/视图 | — | — | snake_case + _table后缀 | — |

**命名核心原则：**
1. 可读性与语义化优先（`user_count` > `uc`）
2. 函数/方法使用动词或动宾结构（`get_user_name`、`calculate_checksum`）
3. 布尔值前缀：`is_`、`has_`、`can_`、`should_`
4. 避免不必要缩写，除非在团队白名单中
5. 优先使用英文标识符

## 版本控制标准

- **分支命名**：`type/description`（feat/、fix/、refactor/、chore/）
- **提交格式**：`type(scope): description`（feat, fix, docs, style, refactor, test, chore）
- **语义化版本**：MAJOR.MINOR.PATCH
- **短生命周期分支**：最长3天
- **AI生成代码**：必须经过人工审查后才能合并
- **每次AI修改前**：必须创建Git checkpoint

## 变更分类

| 等级 | 定义 | 影响范围 | 同步策略 |
|------|------|---------|---------|
| **L1 微小** | 仅内部逻辑 | 单个函数/参数 | AI直接修改代码 |
| **L2 局部** | 接口/数据模型变更 | 模块级 | AI同时修改代码+文档+测试 |
| **L3 架构** | 核心架构/技术选型 | 系统级 | 完整循环（Phase 0→1→2） |

## 硬性规则（不可协商）

1. **审计是强制的** — 每个阶段的输出必须通过AI审计后才能进入人类审查
2. **测试覆盖是强制的** — 没有对应测试的代码不允许提交
3. **文档同步是强制的** — 每次代码变更必须更新对应的文档
4. **外部搜索是强制的** — 在需求和架构阶段之前，AI必须搜索业界最佳实践
5. **小步迭代** — 每个AI任务应在2-5分钟内可完成；大任务必须拆解
6. **验证优先于生成** — 测试和验证是质量瓶颈，在这里投入
7. **代码是事实，文档是描述** — 不一致时同步修改两者；代码是事实来源

## 何时激活

当用户讨论以下话题时自动激活：
- AI主导的软件开发、agentic engineering
- 软件全生命周期管理、SDLC规划
- 需求分析、架构设计、编码实施、测试工程
- 文档交付、变更管理、版本控制
- 项目初始化、Agent配置

## 相关技能

|| 技能 | 阶段 | 激活关键词 ||------|------|-----------|| `ai-led-dev-project-init` | Phase 0 | 项目初始化、Agent配置、SOUL.md、AGENTS.md || `ai-led-dev-requirements` | Phase 1 | 需求工程、PRD、INITIAL.md、需求分析 || `ai-led-dev-architecture` | Phase 2 | 架构设计、技术选型、系统设计 || `ai-led-dev-feature-design` | Phase 2.5 | 功能设计、UI设计、权限设计、原型 || `ai-led-dev-implementation` | Phase 3-4 | 编码实施、TDD、代码生成 || `ai-led-dev-testing` | Phase 5 | 测试工程、测试用例、TDAD、验证优先 || `ai-led-dev-documentation` | Phase 6 | 文档同步、交付文档、用户手册 || `ai-led-dev-change-mgmt` | Phase 7 | 变更管理、迭代、影响分析 || `ai-led-dev-version-control` | Phase 8 | 版本管理、发布、补丁 || `ai-led-dev-quality-audit` | 跨阶段 | 质量审计、审查、审计报告 || `ai-led-dev-user-preference` | 跨阶段 | 用户偏好、技术选型、默认配置、ChromaDB、SQLite3、Ollama || `ai-led-dev-domain-spec` | 跨阶段 | 行业规范、领域知识、业务规则、电力行业 |

## 配置注入机制

本方法论使用**两个配置注入技能**，在各阶段自动注入个性化配置：

### 1. 用户偏好注入 (`ai-led-dev-user-preference`)

**内容**：用户的个人/公司技术栈偏好、编码风格、工具链选择。

**注入时机**：
- Phase 0（项目初始化）：生成默认配置
- Phase 2（架构设计）：提供技术选型默认值
- Phase 4（编码实施）：提供编码风格默认值

**示例**：
- 向量数据库默认使用 ChromaDB
- 关系型数据库默认使用 SQLite3
- AI推理默认使用 Ollama + qwen3.6

### 2. 行业规范注入 (`ai-led-dev-domain-spec`)

**内容**：行业特定的业务规则、数据规范、测试场景。

**注入时机**：
- Phase 1（需求分析）：补充行业特有需求
- Phase 2（架构设计）：考虑行业特定约束
- Phase 3（测试数据）：生成行业特定测试场景
- Phase 4（编码实施）：遵循行业特定业务规则
- Phase 5（测试工程）：验证行业特定边界条件

**示例**：
- 变压器油温≤80℃（电力行业）
- 保护定值规范（过流、差动、零序、距离保护）
- 等保三级合规要求（数据不出内网）

### 配置注入流程图

```
Phase 0: 项目初始化
  ├── 加载 ai-led-dev-user-preference → 生成默认配置
  ├── 加载 ai-led-dev-domain-spec → 补充行业特定需求
  └── 输出: SOUL.md, AGENTS.md, CLAUDE.md

Phase 1: 需求分析
  ├── 加载 ai-led-dev-user-preference → 技术栈默认值
  ├── 加载 ai-led-dev-domain-spec → 行业特有需求
  └── 输出: INITIAL.md

Phase 2: 架构设计
  ├── 加载 ai-led-dev-user-preference → 技术选型默认值
  ├── 加载 ai-led-dev-domain-spec → 行业特定约束
  └── 输出: ARCHITECTURE.md, DATA-MODEL.md

Phase 3-4: 编码实施
  ├── 加载 ai-led-dev-user-preference → 编码风格默认值
  ├── 加载 ai-led-dev-domain-spec → 行业特定业务规则
  └── 输出: 源代码, 单元测试

Phase 5: 测试工程
  ├── 加载 ai-led-dev-user-preference → 测试框架默认值
  ├── 加载 ai-led-dev-domain-spec → 行业特定测试场景
  └── 输出: 测试套件, 测试报告
```
