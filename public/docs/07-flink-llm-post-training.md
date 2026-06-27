# Flink 赋能模型后训练 (LLM Post-Training)

**Exhibition Booth**  
**Theme**: 为模型后训练的长任务提供实时写入与断点容错

---

## Overview

![LLM Post-Training](/images/Weixin%20Image_20260627190235_20_25.jpg)

> Providing Real-Time Writes and Checkpoint Fault Tolerance for Long-Running Post-Training Tasks

---

## Flink 赋能模型后训练数据准备

数据集准备·多模态处理·特征工程 — 为长周期数据任务提供架构级稳定性保障

---

### 行业场景 (Industry Scenarios)

| Scenario | Description |
|----------|-------------|
| **模型服务** | 面向行业客户的 SFT/RLHF 数据集清洗、去重与质量筛选，支撑模型精调迭代 |
| **具身智能** | 多模态传感数据标注对齐与仿真数据加工，构建训练语料 |
| **自动驾驶** | 多传感器数据融合，场景切片与驾驶行为标注，加速感知与决策模型训练 |

---

### 核心挑战 (Core Challenges)

| Challenge | Description |
|-----------|-------------|
| **h 运行周期长** | TB 级多模态数据，单次处理耗时数小时至数天 |
| **$ 资源消耗高** | GPU/CPU 混合调度，重复执行造成巨大资源浪费 |
| **! 中断风险高** | 计划内和计划外资源变更频繁，如待恢复引擎需全量重跑 |

---

### Flink 解决方案

**分布式流计算 + Pipeline 执行 + 检查点机制**

| Solution | Description |
|----------|-------------|
| **零改造，自带检查点** | 无需引入额外 key，无需侵入式改造，自带优秀的检查点机制，中断后从断点无缝继续跑，减少重跑的资源消耗 |
| **逐条流式写入** | Record 级流式处理，部分成功即可落盘，告别批处理 stage-by-stage 部分失败的全量丢弃，减少重跑的资源消耗 |
| **精准断点恢复** | 从最后成功检查点恢复，已写入数据零重算，Exactly-Once 语义保障一致性 |
| **弹性伸缩** | 资源变更不中断正在运行的子任务，保障处理过程的连续性 |
