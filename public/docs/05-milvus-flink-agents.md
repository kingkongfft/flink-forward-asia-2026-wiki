# Milvus + Flink-Agents: 为事件驱动的实时 Agent 提供高性能记忆能力

**Speaker**: 王道远 | 阿里云 Milvus 引擎负责人  
**Session**: June 27 Morning, 大宴会厅  
**Track**: AI Agent

---

## Talk Title

![Title Slide](/images/Weixin%20Image_20260627190243_28_25.jpg)

**Milvus + Flink-Agents**  
为事件驱动的实时 Agent 提供高性能记忆能力

---

## 长时运行 Agent 的两堵墙

![Two Walls](/images/Weixin%20Image_20260627190304_41_25.jpg)

Long-running Agents face two fundamental challenges:

1. **遗忘 (Forgetting)** — Agent loses context over time
2. **知识爆炸 (Knowledge Explosion)** — Too much information to manage

> 长程不是长上下文，而是**跨 session、跨实例、跨月份**经验

---

## 记忆是分层的

![Layered Memory](/images/Weixin%20Image_20260627190306_42_25.jpg)

Memory types in Agent systems:

| Memory Type | Description |
|-------------|-------------|
| **Working Memory** | 当前上下文 (Current context) |
| **Episodic Memory** | 发生过的事件 (Past events) |
| **Semantic Memory** | 长期画像与事实 (Long-term profiles & facts) |
| **Procedural Memory** | 稳定流程 (Stable procedures) |

> 长期记忆 = 按重要性写入，按相关度召回

Warning: 不是把所有历史塞进 prompt

---

## 长期记忆需要服务边界

![Service Boundary](/images/Weixin%20Image_20260627190308_43_25.jpg)

### Approach Comparison:

**Left**: 数据库 + SDK — 成本高，能力不一致
- 画像, 超户, 删除

**Right**: AMS (Agent Memory Service) — 像数据库一样提供记忆服务
- 应用 / Agent
- 标准 API 🔒
- AMS 记忆服务:
  - 持久保存
  - 语义召回 top-k

> Agent 长期记忆是一项**基础设施能力**

---

## AMS 是什么

![AMS Architecture](/images/Weixin%20Image_20260627190311_44_25.jpg)

**Agent Memory Service (AMS)** — The central memory infrastructure for Agents:

### Two Sides:

1. **Agent 侧**
   - 容 API
   - 端长期记忆服务

2. **平台 / 控制台侧**
   - Milvus 控制台 AI 中心

### Key Features:
- 跨 session / 设备 / 实例保留经验
- **底座: 阿里云 Milvus**
