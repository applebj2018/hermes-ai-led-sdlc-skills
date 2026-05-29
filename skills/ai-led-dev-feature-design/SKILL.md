---
name: ai-led-dev-feature-design
description: "Phase 2.5: 功能设计。设计权限模型、工作流、UI组件、设计令牌、可交互原型。"
version: 1.0.0
metadata:
  hermes:
    tags: [feature-design, 功能设计, UI-design, 权限设计, 工作流, 原型, DESIGN-TOKENS]
    related_skills: [ai-led-dev-overview, ai-led-dev-architecture, ai-led-dev-implementation, ai-led-dev-quality-audit]
---

# Phase 2.5: 功能设计

## 何时使用

- 架构设计已批准，需要详细设计核心功能
- 需要设计权限模型、审批流程、版本管理
- 需要设计UI组件和设计令牌
- 需要生成可交互HTML原型

## 核心输出

| 文档 | 用途 |
|------|------|
| PERMISSION-DESIGN.md | 权限模型设计 |
| WORKFLOW-DESIGN.md | 工作流/审批流程设计 |
| UI-COMPONENTS.md | UI组件清单 |
| DESIGN-TOKENS.md | 设计令牌（颜色、字体、间距等） |
| prototypes/index.html | 可交互HTML原型 |

## 权限设计模板

```markdown
# PERMISSION-DESIGN.md — 权限管理设计

## 1. 角色定义
| 角色 | 职责 | 典型用户 |
|------|------|---------|

## 2. 权限矩阵
| 角色 | 查看 | 创建 | 编辑 | 删除 | 审批 | 管理 |
|------|------|------|------|------|------|------|

## 3. 最小权限原则
- 每个角色只拥有完成工作所需的最小权限
- 普通用户默认只读
- 管理员权限分级

## 4. 数据隔离
- 租户隔离策略
- 部门隔离策略
- 项目隔离策略

## 5. 审计日志
- 权限变更日志
- 访问审计日志
- 定期权限审查机制
```

## 工作流设计模板

```markdown
# WORKFLOW-DESIGN.md — 工作流设计

## 1. 核心流程
[描述核心业务流程]

## 2. 状态机
```
stateDiagram-v2
    [*] --> 状态1
    状态1 --> 状态2: 触发条件
    状态2 --> 状态3: 触发条件
    状态2 --> 状态1: 驳回
```

## 3. 审批流程
| 文档类型 | 审批链 | 超时处理 |
|---------|--------|---------|

## 4. 版本管理
- 版本号规则（语义化版本）
- 变更记录字段
- 版本对比功能
- 回滚操作说明
```

## UI设计令牌模板

```css
/* DESIGN-TOKENS.md */
:root {
  /* 品牌色 */
  --brand-primary: #0052D9;
  --brand-primary-light: #EFF6FF;
  --brand-primary-dark: #003D99;

  /* 功能色 */
  --success: #52C41A;
  --warning: #FAAD14;
  --error: #F5222D;
  --info: #1890FF;

  /* 中性色 */
  --neutral-100: #FAFAFA;
  --neutral-200: #F5F5F5;
  --neutral-500: #BFBFBF;
  --neutral-800: #434343;
  --neutral-900: #141414;

  /* 字体 */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 20px;
  --font-size-2xl: 24px;

  /* 间距 */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-base: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;

  /* 圆角 */
  --radius-sm: 4px;
  --radius-base: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* 阴影 */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-base: 0 2px 8px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.15);

  /* 过渡 */
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
  --transition-slow: 350ms ease;
}
```

## UI组件清单模板

```markdown
# UI-COMPONENTS.md — UI组件清单

## 核心组件

### 1. [组件名]
- **用途**: [描述]
- **Props**: [属性列表]
- **状态**: [组件状态]
- **交互**: [用户交互行为]
- **对应页面**: [使用该组件的页面]

### 2. [组件名]
...

## 页面清单

| 页面 | 路由 | 核心组件 | 功能描述 |
|------|------|---------|---------|
```

## HTML原型生成提示词

```text
# 角色
你是一名前端开发专家，擅长快速生成高保真可交互原型。

# 任务
基于 UI-COMPONENTS.md 和 DESIGN-TOKENS.md，生成完整的可交互HTML原型。

# 页面要求
[列出需要原型的核心页面]

# 技术要求
- 使用 HTML/CSS/JS，无需后端，模拟数据硬编码
- 引用 Tailwind CSS CDN 或内联样式
- 尽量接近真实交互（点击菜单切换页面内容）
- 响应式设计
- 微动画和过渡效果

# 输出
完整的HTML代码，保存到 prototypes/index.html
```

## 生成提示词模板

```text
# 角色
你是一名资深功能设计师，擅长设计权限模型、工作流和UI组件。

# 任务
基于 ARCHITECTURE.md 和 INITIAL.md，生成详细的功能设计文档。

**请先搜索互联网**，参考业界类似系统的功能设计最佳实践。

# 输出要求
1. PERMISSION-DESIGN.md — 权限模型
2. WORKFLOW-DESIGN.md — 工作流/审批流程
3. UI-COMPONENTS.md — UI组件清单
4. DESIGN-TOKENS.md — 设计令牌
5. prototypes/index.html — 可交互原型

# 设计原则
- 权限设计遵循最小权限原则
- 工作流设计考虑异常路径
- UI设计现代、动感、体验好
- 组件可复用、粒度合理
```

## 审计提示词模板

```text
# 角色
你是一名功能设计审计专家。

# 审计维度

## 1. 权限设计
- [ ] 是否覆盖所有用户角色？
- [ ] 权限矩阵是否完整（增删改查、审批、管理）？
- [ ] 是否遵循最小权限原则？
- [ ] 是否有权限变更审计？

## 2. 工作流设计
- [ ] 状态机是否闭环？
- [ ] 驳回路径是否完整？
- [ ] 是否有紧急通道？
- [ ] 审批超时如何处理？

## 3. UI设计
- [ ] 设计令牌是否覆盖所有视觉元素？
- [ ] 组件是否覆盖所有核心功能？
- [ ] 组件粒度是否合理？
- [ ] 是否考虑无障碍设计？

## 4. 原型
- [ ] 是否覆盖所有核心页面？
- [ ] 页面间导航是否流畅？
- [ ] 交互是否自然？
- [ ] 视觉是否一致？

# 输出格式
按标准审计报告格式输出。
```

## 人类审批清单

| # | 审批项 | 通过标准 |
|---|--------|---------|
| 1 | 权限设计是否合理 | 最小权限原则、无权限漏洞 |
| 2 | 工作流是否完整 | 状态机闭环、异常路径覆盖 |
| 3 | UI组件是否覆盖核心功能 | 无遗漏组件 |
| 4 | 设计令牌是否一致 | 视觉风格统一 |
| 5 | 原型是否通过用户评审 | 交互逻辑清晰 |
| 6 | 审计报告中的问题是否已修复 | 所有❌项已解决 |

## 执行步骤

1. **读取输入**：读取已批准的 ARCHITECTURE.md 和 INITIAL.md
2. **外部搜索**：搜索同类系统的功能设计最佳实践
3. **权限设计**：生成 PERMISSION-DESIGN.md
4. **工作流设计**：生成 WORKFLOW-DESIGN.md
5. **UI设计**：生成 UI-COMPONENTS.md 和 DESIGN-TOKENS.md
6. **原型生成**：生成可交互HTML原型
7. **提交审计**：将设计文档提交给审计Agent审查
8. **迭代修改**：根据审计报告修改设计
9. **人类审批**：按审批清单逐项检查
10. **版本化**：将最终版纳入版本管理

## 注意事项

- **UI现代感**：使用微动画、过渡效果、渐变、阴影增强视觉层次
- **组件复用**：设计可复用组件，避免重复代码
- **响应式**：原型必须适配不同屏幕尺寸
- **无障碍**：颜色对比度满足WCAG标准
- **用户反馈**：原型生成后让用户预览确认
