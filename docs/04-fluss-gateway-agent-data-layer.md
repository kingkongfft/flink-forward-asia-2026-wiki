# 构建 AI Agent 实时数据层：Fluss Gateway

**Speaker**: 王俊博 | Apache Fluss Contributor  
**Session**: June 27 Morning, 大宴会厅  
**Track**: AI Agent

---

## Talk Title

![Title Slide](../Weixin%20Image_20260627190240_25_25.jpg)

**Fluss Gateway**  
构建 Agent 实时数据层：Fluss Gateway 的设计、实践与演进

---

## Architecture Overview

![Architecture](../Weixin%20Image_20260627190241_26_25.jpg)

### OpenClaw Agent Risk Control Demo (Agent 风控 Demo 与实践)

The architecture demonstrates a complete Agent-based risk control system:

#### Data Flow:
1. **OpenClaw Agent Runtime**
   - Agent 执行器: 规划引擎, LLM调用, 工具执行, 结果写入
   - 事件触发 → Fluss Hook 插件

2. **Fluss Hook 插件**
   - 捕获生命周期事件
   - 实时过滤

3. **Fluss Gateway**
   - 高性能 REST API 网关

4. **Fluss Cluster**
   - 流式存储
   - 实时订阅

5. **AI Function**
   - 风险识别与规则
   - 模型推理调用
   - 模型服务 (Qwen)

6. **风险判定与聚合**
   - 窗口统计, 规则过滤

7. **下游输出**
   - SLS 日志: 审计检查, 告警
   - DLF 数据湖: 业务分析, 合规
   - 钉钉 IM: 高危风险实时告警

---

## Key Components

| Component | Description |
|-----------|-------------|
| **Fluss-hook** | Agent 运行时生命周期事件, 结构化事件流 |
| **Fluss 流式存储** | 高性能 REST Gateway, 支持 CDC 实时订阅, 端到端延迟秒级 |
| **Flink 实时分析** | AI function 调用大模型进行语义级风险研判或者固定CEP规则 |
| **钉钉 IM** | 高危风险输出, 实现秒级告警 |
