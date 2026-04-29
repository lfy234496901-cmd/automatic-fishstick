AI-SRE: 基于 Multi-Agent 的生产级故障自动诊断与自愈系统
📌 项目简介
AI-SRE 是一个基于大语言模型（LLM）驱动的多智能体协同系统。它旨在解决云原生微服务架构下，运维人员面临的“告警疲劳”和“排障链路长”的核心痛点。

本项目模拟了高级 SRE（站点可靠性工程师）的工作流，通过 Watcher（监听）、Investigator（调查） 和 Action（执行） 三个核心 Agent 协作，实现从接收告警到自动定位根因、再到闭环自愈的全流程自动化。

🚀 核心架构与逻辑流
本项目采用 ReAct (Reasoning and Acting) 框架设计，确保 Agent 具备长链推理能力：

Watcher Agent (监控感知):

职责: 实时接入监控 Webhook（如 Prometheus）。

逻辑: 提取告警上下文，判断是否需要启动深度排查，避免无效告警干扰系统。

Investigator Agent (深度推理):

职责: 核心大脑，负责根因分析 (RCA)。

逻辑: 通过 Tool Calling 调用日志系统 (ELK) 和指标系统 (Prometheus)。利用 Chain-of-Thought (CoT) 逻辑进行多轮推理，对比日志报错与性能指标。

Action Agent (自愈执行):

职责: 风险评估与故障修复。

逻辑: 根据诊断报告评估操作风险。对低风险操作（如 Pod 重启、资源扩容）直接通过 K8s API 执行；对高风险操作生成方案并推送到 Slack 待人工审批。

🛠️ 技术栈
语言: Python 3.10+

LLM 驱动: 支持 OpenAI / Gemini API / DeepSeek (可通过环境变量配置)

架构模式: Multi-Agent Orchestration, ReAct Framework

基础设施交互: 模拟 Kubernetes API, Elasticsearch API, Prometheus API
