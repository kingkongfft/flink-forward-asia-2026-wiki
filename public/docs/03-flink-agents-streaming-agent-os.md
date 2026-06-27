# Apache Flink Agents: Streaming Agent OS

**Speaker**: 谢文晋 | 阿里云 Flink 高级研发工程师, Apache Flink Committer  
**Session**: June 27 Morning, 大宴会厅  
**Track**: AI Agent

---

## Talk Title

![Title Slide](/images/Weixin%20Image_20260627190233_17_25.jpg)

**Apache Flink Agents: Streaming Agent OS**  
Event Driven · Distributed · Reliable

---

## Section 01: Agent时代：训练对象从模型走向系统

![Section 01](/images/Weixin%20Image_20260627190236_21_25.jpg)

> 不是"支持Agent"，而是"为Agent而生"的框架设计

**Key Insight**: In the Agent era, the training target shifts from models to systems. The framework is designed *for* Agents, not merely *supporting* Agents.

---

## Why Flink is the Real-Time Data Foundation for Agents

![Why Flink](/images/Weixin%20Image_20260627190242_27_25.jpg)

> Agent系统产生的是**连续事件流**，而不是离线文件

### Three Core Capabilities:

1. **实时事件接入 (Real-Time Event Ingestion)**
   - 用户对话 (User conversations)
   - 工具调用 (Tool invocations)
   - RAG 检索 (RAG retrieval)
   - 反馈事件 (Feedback events)

2. **有状态流处理 (Stateful Stream Processing)**
   - Event Time
   - Window
   - Keyed State
   - Exactly-once

3. **可治理数据资产 (Governable Data Assets)**
   - 特征 (Features)
   - 标签 (Labels)
   - 血缘 (Lineage)
   - 训练队列 (Training queues)

> 核心观点: Flink把线上Agent行为转化为**实时、可靠、可追溯**的训练数据流

---

## Real-World Case: Flink Real-Time Operations Agent

![Flink Ops Agent](/images/Weixin%20Image_20260627190239_24_25.jpg)

### Evolution of Flink Operations:

1. **运维专家 (Ops Expert)** — Flink作业 = 7x24 实时数据流水线
2. **AutoPilot 规则系统** — 规则覆盖已知问题
3. **Flink-Agents 运维 Agent + AMS** — 长尾故障需要Agent

> 连续看护成千上万个作业

---

## Slides from Other Talks (Related Content)

![Slide: What is Agentic](/images/Weixin%20Image_20260627190245_30_25.jpg)

**Speaker**: 蒋晓伟 | 阿里云资深技术专家、Apache Flink PMC

> 为什么 Agent 是"Agentic"而不是"AI"？

Key points:
- **AI (Artificial Intelligence)**: Machine learning, deep learning, neural networks, LLMs — AI is about **Perception** and **Cognition**
- **Agent**: Agents don't just perceive and think — they **act**, using tools, accessing knowledge, executing tasks, and delivering results
- AI is the "brain", Agents are the "hands and feet"
- Key properties: **自主性 (Autonomy)**, **工具调用 (Tool Use)**, **记忆 (Memory)**, **规划 (Planning)**
- Agent = LLM + 工具 + 记忆 + 规划
- An Agent that truly understands "intelligence" should possess: 交互能力, 推理能力, 规划能力, 记忆能力, 学习能力, 工具使用
