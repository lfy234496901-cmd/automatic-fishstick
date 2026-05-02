# Auto-BI-Agent (自动化商业情报分析 Agent)

## 🌟 项目简介
本项目是一个基于大模型协同（结合 GPT 的复杂推理与 Claude 的长文本处理能力）的智能商业情报分析系统。通过多智能体（Multi-Agent）协作架构，系统能够自动完成从“自然语言需求”到“多维数据提取”，再到“深度原因推演”以及“自动化报告分发”的全链路流程。

## 🛠️ 核心架构逻辑
项目采用了典型的 Multi-Agent 架构，各节点通过结构化数据进行通信：

1.  **意图识别与数据提取 Agent (Text-to-SQL)**：将非结构化的业务提问转化为精确的 SQL 查询，从业务数据库中抓取核心指标。
2.  **深度推演分析 Agent (RAG & Chain-of-Thought)**：利用长链条推理（Long-chain Reasoning）对数据异常进行归因，并结合 RAG（检索增强生成）技术，引入外部市场动态和企业内部日志进行综合比对。
3.  **洞察报告生成 Agent**：将分析结论转化为结构化的 Markdown 报告，支持通过 Webhook 自动推送至企业微信/飞书。

🛠️ 技术栈
语言: Python 3.10+

LLM 驱动: 支持 OpenAI / Gemini API / DeepSeek 

架构模式: Multi-Agent Orchestration, ReAct Framework

基础设施交互: 模拟 Kubernetes API, Elasticsearch API, Prometheus API
