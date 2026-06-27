# LlamaFactory: 统一高效训练中台

**Speaker**: 林旭 | Llama-Factory 核心开发者、YOLO-Master 作者  
**Session**: June 27 Morning, 大宴会厅  
**Track**: AI Agent

---

## Talk Title

![Title Slide](/images/Weixin%20Image_20260627190228_12_25.jpg)  
*(See keynote agenda for session details)*

---

## LlamaFactory: Unified Efficient Training Platform

![LlamaFactory Platform](/images/Weixin%20Image_20260627190232_16_25.jpg)

### 核心观点: LlamaFactory不是单一训练框架，而是连接数据、训练、评测与部署的**训练中台**

把治理后的高质量数据，接入训练、对齐、评测与部署的一体化流水线

---

## Pipeline Overview

### 1. Governed Dataset (治理后数据)
- 指令数据 / 偏好数据 / 轨迹数据

### 2. Training Recipe (训练配方)
- SFT / LoRA / QLoRA / Full

### 3. LlamaFactory Core (核心训练引擎)
- 统一 CLI / WebUI / 多模型训练
- **Frameworks**: PyTorch / Hugging Face / DeepSpeed
- **Accelerators**: NVIDIA / Huawei / Hygon

### 4. Alignment & Evaluation (对齐与评测)
- DPO / PPO / GRPO / Benchmark

### 5. Model Artifact (模型产物)
- Checkpoint / Adapter / Export
- **Serving**: vLLM / SGLang / API

---

## 在 Agent 时代的价值

| Value | Description |
|-------|-------------|
| **训练范式统一** | 减少重复工程 |
| **数据闭环接入** | 治理结果快速进入训练 |
| **实验可复用** | 配置、日志、权重分层管理 |
