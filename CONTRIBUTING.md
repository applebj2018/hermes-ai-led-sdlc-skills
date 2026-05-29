# 贡献指南

## 新增技能流程

1. 在 `skills/` 下创建目录，命名格式：`ai-led-sdlc-<主题>`
2. 编写 `SKILL.md`，顶部必须包含 YAML frontmatter：
   ```yaml
   ---
   name: ai-led-sdlc-xxx
   description: "简短描述（60字以内）。"
   version: "1.0.0"
   ---
   ```
3. 在 `catalog.json` 和 `.well-known/skills/index.json` 中注册新技能
4. 运行 `node scripts/validate.mjs` 通过本地校验
5. 提交 PR

## 命名规范

- 目录名：kebab-case，前缀统一为 `ai-led-sdlc-`
- description：一句话，句号结尾，不超过 60 个字符
- 分类（category）：analysis / design / development / quality / docs / process / config
