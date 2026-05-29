---
name: ai-led-dev-user-preference
description: "用户偏好与默认配置。存储个人/公司的技术栈偏好、编码风格、工具链选择。在各阶段作为默认值注入。"
version: 1.0.0
metadata:
  hermes:
    tags: [user-preference, 用户偏好, default-config, 默认配置, tech-preference, 技术偏好]
    related_skills: [ai-led-dev-overview, ai-led-dev-project-init, ai-led-dev-architecture]
---

# 用户偏好与默认配置

## 何时使用

- 项目初始化时，需要确定技术栈默认值
- 架构设计时，需要快速选择技术
- 编码实施时，需要遵循编码风格
- 用户讨论技术选型、默认配置、个人偏好

## 为什么这个技能独立存在

**核心理由**：用户偏好是**跨阶段、跨项目**的个性化配置，与通用方法论正交。

| 维度 | 通用方法论技能 | 本技能 |
|------|--------------|--------|
| 内容 | **怎么做**（流程、方法、模板） | **用什么做**（具体技术选择） |
| 变更频率 | 低（方法论稳定） | 中（技术偏好可能变化） |
| 适用范围 | 所有项目 | 用户的所有项目 |
| 示例 | "先写测试再写代码" | "默认使用 ChromaDB" |

**激活机制**：
- Phase 0（项目初始化）：自动加载，生成默认配置
- Phase 2（架构设计）：自动加载，提供技术选型默认值
- Phase 4（编码实施）：自动加载，提供编码风格默认值
- 用户提到"技术选型"、"默认配置"时：手动激活

## 用户技术栈偏好

### 数据库偏好

| 类型 | 默认选择 | 说明 |
|------|---------|------|
| **向量数据库** | ChromaDB | 轻量、嵌入式、适合原型和中小规模 |
| **关系型数据库** | SQLite3 | 零配置、嵌入式、适合中小型项目 |
| **缓存** | Redis | 行业标准、高性能 |

**何时使用备选方案**：
- 数据量 > 100万条 → 考虑 Milvus/Qdrant 替代 ChromaDB
- 需要多租户/高并发 → 考虑 PostgreSQL 替代 SQLite3
- 需要分布式部署 → 考虑 MinIO 替代本地存储

### AI 模型偏好

| 用途 | 默认选择 | 加载命令 |
|------|---------|---------|
| **本地推理** | Ollama + qwen3.6-low-temp | `ollama run qwen3.6-low-temp:latest` |
| **文本嵌入** | Ollama + nomic-embed-text | `ollama run nomic-embed-text` |
| **重排序** | Ollama + bge-reranker | `ollama run bge-reranker` |

**Ollama 使用规范**：
```bash
# 列出已安装模型
ollama list

# 拉取模型
ollama pull qwen3.6-low-temp:latest

# 运行推理
ollama run qwen3.6-low-temp:latest "你的问题"

# 通过 API 调用
curl http://localhost:11434/api/generate -d '{
  "model": "qwen3.6-low-temp:latest",
  "prompt": "你的问题"
}'
```

### 开发工具偏好

| 工具类型 | 默认选择 | 说明 |
|---------|---------|------|
| **包管理** | pip + conda | Conda 管理环境，pip 安装包 |
| **代码格式化** | ruff | 快速、统一 |
| **类型检查** | pyright | 微软出品、严格模式 |
| **测试框架** | pytest | 行业标准 |
| **版本控制** | Git | 行业标准 |
| **容器化** | **禁止 Docker** | 使用原生运行 + Conda |

## 编码风格偏好

### Python 编码风格

```python
# 命名规范（必须遵循）
variable_name = "snake_case"      # 变量/函数
ClassName = "PascalCase"          # 类/接口
CONSTANT_NAME = 42                # 常量
_private_var = "私有变量"          # 私有成员

# 类型注解（必须）
def calculate_score(
    items: list[dict[str, Any]],
    threshold: float = 0.7
) -> float:
    """计算评分。

    Args:
        items: 评分项列表
        threshold: 阈值，默认0.7

    Returns:
        最终评分
    """
    pass

# 代码规模限制
# - 函数 ≤ 50行
# - 类 ≤ 500行
# - 文件 ≤ 1000行

# 注释语言
# - 所有注释使用中文
# - 解释为什么（why），不解释做什么（what）
```

### 数据库命名规范

```sql
-- 表命名: snake_case + _table 后缀
CREATE TABLE user_table (
    user_id BIGINT PRIMARY KEY,
    user_name VARCHAR(200) NOT NULL
);

-- 索引命名: idx_表名_字段名
CREATE INDEX idx_user_table_user_name ON user_table(user_name);

-- 视图命名: 实体_view
CREATE VIEW user_detail_view AS ...;
```

## 配置注入方式

### 方式1：对话中声明（推荐）

```
用户: 新项目，用默认配置
AI: 已加载默认配置：
    - 向量数据库: ChromaDB
    - 关系型数据库: SQLite3
    - AI推理: Ollama + qwen3.6
    ...
```

### 方式2：覆盖默认值

```
用户: 新项目，但用 PostgreSQL 代替 SQLite3
AI: 已更新配置：
    - 向量数据库: ChromaDB（默认）
    - 关系型数据库: PostgreSQL（覆盖）
    - AI推理: Ollama + qwen3.6（默认）
    ...
```

### 方式3：项目配置文件

在项目根目录创建 `project_config.yaml`：

```yaml
# project_config.yaml
tech_stack:
  database:
    vector: "chromadb"
    relational: "sqlite3"  # 可改为 "postgresql"
  ai:
    inference: "ollama/qwen3.6-low-temp:latest"
    embedding: "ollama/nomic-embed-text"
  backend:
    framework: "fastapi"
  frontend:
    framework: "react+typescript"
    ui_library: "ant-design"
```

## 在 AGENTS.md 中的注入模板

生成 AGENTS.md 时，自动注入以下配置段：

```markdown
## 技术栈配置（用户偏好）
- 向量数据库: ChromaDB
- 关系型数据库: SQLite3
- AI推理: Ollama (qwen3.6-low-temp:latest)
- 嵌入模型: Ollama (nomic-embed-text)
- 后端框架: FastAPI
- 前端框架: React + TypeScript
- UI组件库: Ant Design
- 包管理: pip + conda
- 代码格式化: ruff
- 类型检查: pyright
- 测试框架: pytest
- 容器化: 禁止Docker，使用原生运行
```

## 注意事项

- **默认值可覆盖**：所有默认值都可以在项目级别覆盖
- **禁止 Docker**：这是硬性规则，所有环境使用原生运行
- **本地优先**：优先使用本地部署方案（Ollama、SQLite、ChromaDB）
- **Conda 环境**：使用 Conda 管理 Python 环境
- **配置透明**：所有配置在 AGENTS.md 中明确声明
- **与行业规范分离**：本技能只包含技术偏好，行业规范见 `ai-led-dev-domain-spec`
