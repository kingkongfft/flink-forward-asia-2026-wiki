# 腾讯基于 Flink 2.x 打造 AI 计算引擎的探索与实践

**Speakers**: 陈子豪 | 腾讯实时计算高级研发工程师、Flink Contributor, 张作峰 | 腾讯专家工程师、InLong Committer、Flink Contributor  
**Session**: June 27 Afternoon, 大宴会厅  
**Track**: 平台AI实践

---

## Talk Title

![Title Slide](/images/Weixin%20Image_20260627190356_52_25.jpg)

**腾讯基于 Flink 2.x 打造 AI 计算引擎的探索与实践**

---

## AI 时代的数据诉求与 Flink 破局之道

**Speakers**: 罗瑞脩, 李昊哲 | 阿里云实时计算 Flink 高级产品经理  
**Session**: June 27 Afternoon, 大宴会厅  
**Track**: 平台AI实践

![AI Data Needs](/images/Weixin%20Image_20260627190358_53_25.jpg)

---

## SQL 层 AI 能力: 一条 SQL 完成全表情感分析

![SQL AI Capability](/images/Weixin%20Image_20260627190402_55_25.jpg)

### 2.1 SQL 层 AI 能力 ③ 一条 SQL 完成全表情感分析

六大函数都经 LATERAL TABLE 展开，同时支持位置参数与命名参数。

```sql
-- 整张评论表逐行情感分析
SELECT t.*
FROM comments,
LATERAL TABLE (
    AI_SENTIMENT('qwen3.6-flash', content)
) AS t;
```

✓ 一条 SQL = 全表情感分析

两种参数模式:
- 位置参数
- 命名参数

按需选择使用方式。

---

## Flink AI Ops 开启开发新时代

![Flink AI Ops](/images/Weixin%20Image_20260627190404_56_25.jpg)

### 03 Flink AI Ops开启开发

智能助手 × 智能巡检 · 双模式 · 全面覆盖实时计算
