# Flink Forward Asia 2026 — Conference Notes

> **Real-Time Data Powers the Future of AI**  
> Shenzhen, June 26–27, 2026 | Organized by Alibaba Cloud

---

## Document Index

| File | Topic | Speakers/Source |
|------|-------|-----------------|
| [00-conference-overview.md](00-conference-overview.md) | Conference overview, venue, theme | — |
| [01-keynote-agenda.md](01-keynote-agenda.md) | Keynote agenda (June 26 morning) | 李飞飞, 王峰, 陈川, 李博杰, 刘湘雯, 汪军华, 朱熙文, 李劲松, 张子良, 张静, 伍狮, 刘煊, 王沛斌 |
| [02-track-agendas.md](02-track-agendas.md) | Track/sub-forum agendas (all sessions) | — |
| [03-flink-agents-streaming-agent-os.md](03-flink-agents-streaming-agent-os.md) | Apache Flink Agents: Streaming Agent OS | 谢文晋 (Apache Flink Committer) |
| [04-fluss-gateway-agent-data-layer.md](04-fluss-gateway-agent-data-layer.md) | Fluss Gateway: Agent实时数据层 | 王俊博 (Apache Fluss Contributor) |
| [05-milvus-flink-agents.md](05-milvus-flink-agents.md) | Milvus + Flink-Agents: Agent记忆能力 | 王道远 (阿里云 Milvus 引擎负责人) |
| [06-llamafactory-training-platform.md](06-llamafactory-training-platform.md) | LlamaFactory: 统一高效训练中台 | 林旭 (Llama-Factory 核心开发者) |
| [07-flink-llm-post-training.md](07-flink-llm-post-training.md) | Flink赋能模型后训练 (LLM Post-Training) | Exhibition booth |
| [08-nvidia-flink-multimodal.md](08-nvidia-flink-multimodal.md) | NVIDIA+阿里云 Flink多模态流处理 + AI算力终端 | 陈川 (NVIDIA) |
| [09-alibaba-cloud-agentic-cloud.md](09-alibaba-cloud-agentic-cloud.md) | Alibaba Cloud Agentic Cloud 架构 | Exhibition booth |
| [10-flink-autopilot-agent.md](10-flink-autopilot-agent.md) | Flink全自动运维 AutoPilot | 苏轩楠 (Flink Committer), 常胜波 |
| [11-tencent-flink-ai-engine.md](11-tencent-flink-ai-engine.md) | 腾讯Flink 2.x AI引擎 + Flink AI Ops | 陈子豪, 张作峰 (腾讯), 罗瑞脩, 李昊哲 (阿里云) |

---

## Key Themes

### 1. Flink as the Real-Time Data Foundation for AI Agents
- Agent systems generate **continuous event streams**, not offline files
- Flink provides: real-time event ingestion → stateful stream processing → governable data assets

### 2. Agentic Architecture Patterns
- **Fluss Gateway**: Agent → Fluss Hook → Fluss Gateway → Flink → AI Function → Risk Assessment
- **Milvus AMS**: Agent Memory Service for cross-session, cross-device, cross-month memory
- **LlamaFactory**: Training pipeline connecting data governance → training → evaluation → deployment

### 3. NVIDIA + Flink Multimodal Processing
- Live sports commentary pipeline: Video → VLM → LLM → TTS → Audio sync
- Flink Agentic operators for dynamic scheduling

### 4. Agent Memory Architecture
- Layered memory: Working → Episodic → Semantic → Procedural
- Long-term memory = write by importance, recall by relevance
- AMS (Agent Memory Service) as infrastructure capability

### 5. Platform AI Practices
- Tencent: Flink 2.x as AI computing engine
- Alibaba Cloud: SQL-level AI capabilities (AI_SENTIMENT, LATERAL TABLE)
- Flink AI Ops: Intelligent assistant × intelligent patrol dual-mode
