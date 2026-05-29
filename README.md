# hermes-ai-led-dev-skills

AI-led 软件开发全流程 Hermes Agent Skills 集合。

覆盖从 **需求分析 → 架构设计 → 功能设计 → 代码实现 → 质量审计 → 测试 → 发布 → 文档维护** 的完整 DevOps 链路，为 Hermes Agent 提供结构化的开发工作流指导。

## 📦 技能清单

| 技能名 | 类别 | 说明 |
|--------|------|------|
| `ai-led-dev-architecture` | design | AI驱动的系统架构设计，包含技术选型、模块划分与接口定义。 |
| `ai-led-dev-change-mgmt` | process | AI驱动的变更管理流程，控制需求变更、影响分析与回滚策略。 |
| `ai-led-dev-documentation` | docs | AI驱动的技术文档自动生成与维护，保持代码与文档同步。 |
| `ai-led-dev-domain-spec` | design | AI驱动的领域模型与业务规范定义，统一团队业务语言。 |
| `ai-led-dev-feature-design` | design | AI驱动的功能设计流程，输出PRD、流程图与状态机。 |
| `ai-led-dev-implementation` | development | AI驱动的代码实现指导，含编码规范、重构建议与最佳实践。 |
| `ai-led-dev-overview` | process | AI驱动开发方法论总览，定义全流程框架与角色职责。 |
| `ai-led-dev-project-init` | development | AI驱动的项目初始化，含仓库搭建、目录结构与技术栈配置。 |
| `ai-led-dev-quality-audit` | quality | AI驱动的质量审计，覆盖代码质量、安全扫描与性能基线。 |
| `ai-led-dev-requirements` | analysis | AI驱动的需求分析，用户故事拆分、验收标准与优先级排序。 |
| `ai-led-dev-testing` | quality | AI驱动的测试策略，单元测试、集成测试与自动化测试生成。 |
| `ai-led-dev-user-preference` | config | AI驱动的用户偏好管理，个性化配置与上下文记忆维护。 |
| `ai-led-dev-version-control` | development | AI驱动的版本控制规范，分支策略、提交规范与发布流程。 |

## 🚀 快速开始

### 方式一：Hermes CLI 直接安装（推荐）

```bash
hermes skills install https://github.com/liushengli/hermes-ai-led-dev-skills
```

### 方式二：手动克隆到本地

```bash
git clone https://github.com/liushengli/hermes-ai-led-dev-skills.git
cp -r hermes-ai-led-dev-skills/skills/* ~/.hermes/skills/
```

### 方式三：配置外部目录（不复制文件，实时同步）

在 `~/.hermes/config.yaml` 中添加：

```yaml
skills:
  external_dirs:
    - ~/hermes-ai-led-dev-skills/skills
```

## 📁 仓库结构

```
hermes-ai-led-dev-skills/
├── README.md
├── LICENSE
├── catalog.json              # 技能目录索引
├── .well-known/skills/       # Agent Skills 发现协议入口
│   └── index.json
├── skills/                   # 所有技能
│   ├── ai-led-dev-requirements/
│   │   └── SKILL.md
│   ├── ai-led-dev-architecture/
│   │   └── SKILL.md
│   └── ...
├── .github/workflows/        # CI 自动校验
│   └── validate.yml
└── scripts/
    └── validate.mjs          # 本地校验脚本
```

## 🛠 本地校验

```bash
node scripts/validate.mjs
```

## 🤝 贡献

欢迎提交 Issue 或 PR。新增技能时请确保：
1. 目录名使用 `ai-led-dev-xxx` 格式
2. 必须包含 `SKILL.md`，顶部有 YAML frontmatter
3. 在 `catalog.json` 和 `.well-known/skills/index.json` 中注册

## 📄 协议

MIT License
