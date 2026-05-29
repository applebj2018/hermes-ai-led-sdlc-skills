---
name: ai-led-sdlc-domain-spec
description: "行业规范与领域知识。存储行业特定的业务规则、数据规范、测试场景。在设计、测试、编码阶段自动注入。"
version: 1.0.0
metadata:
  hermes:
    tags: [domain-spec, 行业规范, domain-knowledge, 领域知识, industry-standard, 行业标准]
    related_skills: [ai-led-sdlc-overview, ai-led-sdlc-requirements, ai-led-sdlc-architecture, ai-led-sdlc-testing]
---

# 行业规范与领域知识

## 何时使用

- 需求分析阶段，需要补充行业特有的需求
- 架构设计阶段，需要考虑行业特定的约束
- 测试数据生成阶段，需要生成行业特定的测试场景
- 编码实施阶段，需要遵循行业特定的业务规则
- 质量审计阶段，需要检查是否符合行业规范
- 用户讨论行业规范、业务规则、领域知识

## 为什么这个技能独立存在

**核心理由**：行业规范是**领域知识**，与通用方法论正交，需要在多个阶段被引用。

| 维度 | 通用方法论技能 | 本技能 |
|------|--------------|--------|
| 内容 | **怎么做**（流程、方法） | **做什么**（行业特定规则） |
| 适用范围 | 所有行业 | 特定行业 |
| 变更频率 | 低 | 中（行业规范可能更新） |
| 示例 | "先写测试再写代码" | "变压器油温≤80℃" |

**激活机制**：
- Phase 1（需求分析）：自动加载，补充行业特有需求
- Phase 2（架构设计）：自动加载，考虑行业特定约束
- Phase 3（测试数据）：自动加载，生成行业特定测试场景
- Phase 4（编码实施）：自动加载，遵循行业特定业务规则
- Phase 5（测试工程）：自动加载，验证行业特定边界条件
- 用户提到"行业规范"、"业务规则"时：手动激活

## 行业规范结构

本技能以**电力行业**为例，但结构通用，可扩展到其他行业。

### 电力行业规范

#### 1. 设备运行参数规范

| 设备类型 | 参数 | 正常范围 | 警告阈值 | 危险阈值 | 单位 |
|---------|------|---------|---------|---------|------|
| **变压器** | 油温 | 20-70 | 70-80 | >80 | ℃ |
| **变压器** | 负载率 | 0-80 | 80-90 | >90 | % |
| **变压器** | 绕组温度 | 20-90 | 90-105 | >105 | ℃ |
| **断路器** | 分闸时间 | 0-60 | 60-80 | >80 | ms |
| **断路器** | 合闸时间 | 0-80 | 80-100 | >100 | ms |
| **电流互感器** | 二次电流 | 0-5 | 5-10 | >10 | A |
| **电压互感器** | 二次电压 | 95-105 | 85-95/105-115 | <85/>115 | V |

#### 2. 保护定值规范

| 保护类型 | 定值参数 | 典型值 | 说明 |
|---------|---------|--------|------|
| **过流保护** | 动作电流 | 1.2-1.5倍额定电流 | 躲过最大负荷电流 |
| **过流保护** | 动作时间 | 0.3-0.5s | 与下级保护配合 |
| **差动保护** | 启动电流 | 0.3-0.5倍额定电流 | 躲过不平衡电流 |
| **差动保护** | 制动系数 | 0.3-0.5 | 防止外部故障误动 |
| **零序保护** | 动作电流 | 0.1-0.3A | 接地故障检测 |
| **距离保护** | Ⅰ段定值 | 80-85%线路阻抗 | 速动段 |
| **距离保护** | Ⅱ段定值 | 120-130%线路阻抗 | 延时段 |

#### 3. 通信协议规范

| 协议 | 用途 | 端口 | 说明 |
|------|------|------|------|
| **IEC 61850** | 变电站通信 | 102 | 标准化通信协议 |
| **IEC 104** | 远动通信 | 2404 | 调度自动化 |
| **Modbus TCP** | 设备通信 | 502 | 通用工业协议 |
| **MQTT** | 消息队列 | 1883 | 轻量级消息协议 |

#### 4. 安全规范

| 规范类型 | 要求 | 说明 |
|---------|------|------|
| **等保三级** | 数据不出内网 | 所有数据本地存储 |
| **等保三级** | 访问控制 | 最小权限原则 |
| **等保三级** | 审计日志 | 全量操作日志 |
| **等保三级** | 数据加密 | 敏感数据加密存储 |
| **电力安全** | 防误操作 | 五防逻辑 |
| **电力安全** | 数据完整性 | 校验和验证 |

### 行业特定测试场景

#### 1. 正常场景

```json
{
  "test_suite": "power_equipment_normal",
  "cases": [
    {
      "test_id": "PWR-NORM-001",
      "description": "变压器正常运行",
      "input": {
        "device_type": "变压器",
        "oil_temp": 65.0,
        "load_rate": 75.0,
        "winding_temp": 85.0
      },
      "expected_output": {
        "status": "normal",
        "alert_level": "none"
      }
    },
    {
      "test_id": "PWR-NORM-002",
      "description": "断路器正常分合闸",
      "input": {
        "device_type": "断路器",
        "operation": "分闸",
        "response_time_ms": 45
      },
      "expected_output": {
        "status": "success",
        "within_spec": true
      }
    }
  ]
}
```

#### 2. 边界场景

```json
{
  "test_suite": "power_equipment_boundary",
  "cases": [
    {
      "test_id": "PWR-BOUND-001",
      "description": "变压器油温接近警告阈值",
      "input": {
        "device_type": "变压器",
        "oil_temp": 78.5,
        "load_rate": 85.0
      },
      "expected_output": {
        "status": "warning",
        "alert_level": "yellow",
        "message": "油温接近警告阈值"
      }
    },
    {
      "test_id": "PWR-BOUND-002",
      "description": "变压器油温超过危险阈值",
      "input": {
        "device_type": "变压器",
        "oil_temp": 82.0,
        "load_rate": 92.0
      },
      "expected_output": {
        "status": "danger",
        "alert_level": "red",
        "message": "油温超过危险阈值，立即处理"
      }
    }
  ]
}
```

#### 3. 异常场景

```json
{
  "test_suite": "power_equipment_abnormal",
  "cases": [
    {
      "test_id": "PWR-ABN-001",
      "description": "CT饱和场景",
      "input": {
        "device_type": "电流互感器",
        "secondary_current": 60.0,
        "rated_current": 5.0
      },
      "expected_output": {
        "status": "ct_saturation",
        "alert_level": "red",
        "message": "CT饱和警告，保护可能误动"
      }
    },
    {
      "test_id": "PWR-ABN-002",
      "description": "谐波畸变场景",
      "input": {
        "device_type": "电压互感器",
        "harmonic_content_5th": 15.0,
        "harmonic_content_7th": 8.0
      },
      "expected_output": {
        "status": "harmonic_distortion",
        "alert_level": "yellow",
        "message": "谐波含量超标"
      }
    },
    {
      "test_id": "PWR-ABN-003",
      "description": "零序电流异常",
      "input": {
        "device_type": "零序电流互感器",
        "zero_sequence_current": 0.5,
        "imbalance_ratio": 35.0
      },
      "expected_output": {
        "status": "zero_sequence_alert",
        "alert_level": "yellow",
        "message": "零序电流异常，三相不平衡"
      }
    }
  ]
}
```

#### 4. 降级场景

```json
{
  "test_suite": "power_equipment_degradation",
  "cases": [
    {
      "test_id": "PWR-DEG-001",
      "description": "通信超时场景",
      "input": {
        "device_type": "任意设备",
        "communication_timeout": true,
        "retry_count": 3
      },
      "expected_output": {
        "status": "communication_timeout",
        "fallback": "使用缓存数据",
        "alert_level": "yellow"
      }
    },
    {
      "test_id": "PWR-DEG-002",
      "description": "数据缺失场景",
      "input": {
        "device_type": "传感器",
        "data_missing_ratio": 40.0,
        "missing_fields": ["temperature", "pressure"]
      },
      "expected_output": {
        "status": "data_incomplete",
        "fallback": "规则诊断模式",
        "alert_level": "yellow"
      }
    }
  ]
}
```

## 行业规范在各阶段的注入

### Phase 1: 需求分析

在生成 INITIAL.md 时，自动注入行业特有需求：

```markdown
## 行业特定需求
- 设备运行参数监控（变压器油温、负载率等）
- 保护定值管理（过流、差动、零序、距离保护）
- 通信协议支持（IEC 61850、IEC 104、Modbus）
- 等保三级合规要求
- 电力安全五防逻辑
```

### Phase 2: 架构设计

在生成 ARCHITECTURE.md 时，考虑行业特定约束：

```markdown
## 行业特定架构约束
- 数据不出内网（等保三级）
- 实时性要求（保护动作<50ms）
- 数据完整性（校验和验证）
- 高可用性（99.99%）
```

### Phase 3: 测试数据生成

在生成测试数据时，注入行业特定场景：

```markdown
## 行业特定测试场景
- CT饱和测试
- 谐波畸变测试
- 零序电流异常测试
- 通信超时降级测试
- 数据缺失降级测试
```

### Phase 4: 编码实施

在生成代码时，遵循行业特定业务规则：

```python
# 变压器油温检查（行业规范）
def check_transformer_oil_temp(oil_temp: float) -> AlertLevel:
    """检查变压器油温。

    行业规范:
    - 正常: 20-70℃
    - 警告: 70-80℃
    - 危险: >80℃
    """
    if oil_temp > 80:
        return AlertLevel.DANGER
    elif oil_temp > 70:
        return AlertLevel.WARNING
    else:
        return AlertLevel.NORMAL
```

### Phase 5: 测试工程

在生成测试用例时，覆盖行业特定边界：

```python
# 变压器油温边界测试
@pytest.mark.parametrize("oil_temp,expected_level", [
    (65.0, AlertLevel.NORMAL),      # 正常
    (70.0, AlertLevel.WARNING),     # 警告边界
    (75.0, AlertLevel.WARNING),     # 警告
    (80.0, AlertLevel.DANGER),      # 危险边界
    (85.0, AlertLevel.DANGER),      # 危险
])
def test_transformer_oil_temp_check(oil_temp, expected_level):
    result = check_transformer_oil_temp(oil_temp)
    assert result == expected_level
```

## 扩展其他行业

本技能结构通用，可扩展到其他行业。扩展方式：

### 1. 添加新行业章节

```markdown
## [行业名称]规范

### 1. [规范类别]
| 参数 | 正常范围 | 警告阈值 | 危险阈值 | 单位 |
|------|---------|---------|---------|------|

### 2. 行业特定测试场景
[JSON格式的测试用例]
```

### 2. 在 AGENTS.md 中声明行业

```markdown
## 行业规范
- 行业: 电力行业
- 等保等级: 三级
- 特定规范: IEC 61850, IEC 104
- 数据不出内网: 是
```

**详细说明**：见 `references/domain-knowledge-injection-pattern.md`

## 注意事项

- **行业规范是业务规则**：不是技术实现，是业务约束
- **规范可能更新**：定期更新行业规范
- **与通用规范分离**：行业规范独立于通用方法论
- **测试数据基于规范**：行业特定测试场景从规范派生
- **代码遵循规范**：行业特定业务逻辑在代码中实现
- **审计检查规范**：质量审计时验证是否符合行业规范
