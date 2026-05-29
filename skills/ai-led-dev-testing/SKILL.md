---
name: ai-led-dev-testing
description: "Phase 5: 测试工程。支持TDD和Test-last，TDAD影响分析，四层测试体系，验证优先。"
version: 1.0.0
metadata:
  hermes:
    tags: [testing, 测试工程, TDD, TDAD, 验证优先, 测试用例, 回归测试, 覆盖率]
    related_skills: [ai-led-dev-overview, ai-led-dev-implementation, ai-led-dev-quality-audit]
---

# Phase 5: 测试工程

## 何时使用

- 代码已实现，需要系统化测试
- 需要生成测试用例
- 需要构建TDAD映射
- 需要执行回归测试策略
- 用户讨论测试、验证、覆盖率

## 核心理念

**验证是AI时代的新质量瓶颈。** 代码生成变得容易，但验证变得困难。

### AI改代码的三大风险

| 风险 | 描述 | 后果 | 缓解 |
|------|------|------|------|
| **功能遗漏** | AI"优化"时省略已有功能 | 原有功能消失 | 全量回归测试 |
| **逻辑替换** | AI用"等价"逻辑替换，实际不等价 | 边界条件失效 | 边界测试数据 |
| **幻觉编码** | AI编造不存在的API或库 | 运行时崩溃 | 编译检查+集成测试 |

## 四层测试体系

```
第一层: 单元测试 (Unit Tests)
  ├── 核心函数全覆盖
  ├── Mock外部依赖
  ├── 执行时间: < 5分钟
  └── 频率: 每次代码变更

第二层: 集成测试 (Integration Tests)
  ├── 服务间交互
  ├── 数据库操作
  ├── 执行时间: < 15分钟
  └── 频率: 每日

第三层: 功能验证 (E2E Tests)
  ├── 端到端流程
  ├── 自动化: Playwright/Selenium
  ├── 执行时间: < 30分钟
  └── 频率: 每次发布前

第四层: 安全测试 (Security Tests)
  ├── OWASP Top 10
  ├── 权限穿透测试
  ├── 执行时间: < 1小时
  └── 频率: 每周 + 发布前
```

## 测试用例生成提示词

```text
# 角色
你是一名资深测试工程师。

# 任务
基于设计文档，生成全面的测试用例。

# 输入
[DESIGN.md片段，包含输入字段类型、取值范围、业务规则、边界条件]

# 输出要求

## 1. 正常场景测试用例
- 至少3条，覆盖典型业务场景
- 每条包含: test_id, description, input_data, expected_output

## 2. 边界场景测试用例
- 至少5条，覆盖所有边界值（最小值、最大值、临界点两侧）
- 每条包含: test_id, description, input_data, expected_output

## 3. 异常场景测试用例
- 至少4条，覆盖: null值、类型错误、超出范围、格式错误、SQL注入样本
- 每条包含: test_id, description, input_data, expected_error

## 4. 安全场景测试用例
- SQL注入、XSS、权限越权、敏感信息泄露
- 每条包含: test_id, description, input_data, expected_behaviour

# 输出格式
JSON格式
```

## TDAD映射（Test-Driven Agentic Development）

TDAD给AI一张"函数→测试"对照表。改哪里，测哪里。

### 生成TDAD映射

```bash
# 1. 生成测试列表
pytest --co -q > test_list.txt

# 2. AI分析代码依赖，生成映射
# 输出 tdad_map.json
```

### TDAD映射示例

```json
{
  "module.function_a": [
    "tests/test_module.py::test_function_a_normal",
    "tests/test_module.py::test_function_a_boundary",
    "tests/test_module.py::test_function_a_error"
  ],
  "module.function_b": [
    "tests/test_module.py::test_function_b_normal",
    "tests/test_module.py::test_function_b_integration"
  ]
}
```

### 在AGENTS.md中添加TDAD规则

```markdown
## TDAD测试规则（强制执行）
1. 每次修改代码后，**必须**读取 `tdad_map.json`
2. 找到本次修改的函数名，运行对应的测试列表
3. 如果测试失败，修复代码或更新测试，直到全部通过
4. 没有找到映射的函数，运行该模块的所有测试
```

## 分层回归测试策略

```
Level 0: 冒烟测试 (< 2分钟)
  → 10个核心功能点，每次提交必跑

Level 1: 受影响模块测试 (< 10分钟)
  → AI分析diff，确定受影响的模块
  → 只运行相关模块的单元测试

Level 2: 集成测试 (< 30分钟)
  → 每日自动运行
  → 覆盖所有服务间交互

Level 3: 全量回归 (< 2小时)
  → 每周运行 + 版本发布前运行
  → 覆盖全部测试用例
```

## 验证优先测试

**传统测试 vs 验证优先测试：**

| 对比维度 | 传统测试 | 验证优先测试 |
|---------|---------|-------------|
| 测试目标 | 验证语法正确性 | 验证语义正确性 |
| 测试重点 | 代码能否运行 | 代码是否满足业务需求 |
| 测试方法 | 单元测试、集成测试 | 语义验证、行为验证 |
| 测试时机 | 编码后 | 编码前(TDD) + 编码中(持续验证) |

### 验证规则示例

```python
# 业务规则：搜索结果必须包含至少3个相关文档
def verify_search_results(query, results):
    assert len(results) >= 3, f"搜索结果太少: {len(results)} < 3"

    # 语义验证：每个结果必须与查询相关
    for result in results:
        assert result['relevance_score'] > 0.7, f"相关性太低"

    # 业务规则：机密文档必须按权限过滤
    for result in results:
        assert not result['is_confidential'] or result['user_has_permission'], \
            "机密文档未正确过滤"
```

## 测试审计提示词

```text
# 角色
你是一名测试用例审计专家。

# 审计维度

## 1. 覆盖度
- [ ] 是否覆盖了设计文档中定义的所有输入字段？
- [ ] 是否覆盖了所有业务规则？
- [ ] 正常场景数量是否足够（至少3条）？

## 2. 边界完整性
- [ ] 是否覆盖了所有边界值（最小值、最大值、临界点两侧）？
- [ ] 边界场景数量是否足够（至少5条）？
- [ ] 是否覆盖了空值、null、零值？

## 3. 异常充分性
- [ ] 是否覆盖了常见的异常输入？
- [ ] 异常场景数量是否足够（至少4条）？
- [ ] 是否覆盖了SQL注入、XSS等安全攻击？

## 4. 业务场景
- [ ] 是否覆盖了所有用户角色的操作？
- [ ] 是否覆盖了权限矩阵中的关键权限组合？
- [ ] 是否覆盖了审批流程的关键节点？

# 输出格式
按标准审计报告格式输出。
```

## 人类审批清单

| # | 审批项 | 通过标准 |
|---|--------|---------|
| 1 | 测试覆盖度是否达标 | 审计报告无❌项 |
| 2 | 边界场景是否完整 | 覆盖所有关键字段边界 |
| 3 | 安全测试是否通过 | 无高危漏洞 |
| 4 | 回归测试策略是否合理 | 分层回归方案可行 |
| 5 | TDAD映射是否完整 | 核心函数全覆盖 |
| 6 | 审计报告中的问题是否已修复 | 所有❌项已解决 |

## 执行步骤

1. **生成测试用例**：基于设计文档生成全面测试用例
2. **审计测试用例**：提交给审计Agent审查覆盖度
3. **迭代补充**：根据审计报告补充测试用例
4. **构建TDAD映射**：生成函数→测试对照表
5. **执行测试**：运行四层测试体系
6. **生成报告**：输出测试报告和覆盖率分析
7. **人类审批**：按审批清单逐项检查

## 注意事项

- **测试是安全网**：不要跳过测试，AI改代码可能遗漏功能
- **边界优先**：边界条件是最容易出问题的地方
- **安全测试不可跳过**：SQL注入、XSS、权限越权必须测试
- **TDAD映射维护**：每次添加新功能时更新映射
- **回归策略**：不要每次都跑全量测试，使用分层策略
