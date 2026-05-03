# TechStream AI: Multi-Agent Technical Analysis System

## 项目定位
TechStream 旨在通过多 AI 智能体协作，将碎片化的技术信息转化为深度、严谨的技术白皮书。

## 技术栈
- **LLM:** Gemini 1.5 Pro / GPT-4o
- **Orchestration:** LangGraph (State-based workflow)
- **Tools:** Tavily Search API, GitPython, Markdown-it

## 核心亮点
1. **反馈闭环 (Feedback Loop):** 引入 Critic Agent 机制，确保 AI 不会因首轮生成的简单答案而停止思考。
2. **异构协作:** Researcher 负责广度，Code Analyst 负责深度，Writer 负责表达。
3. **确定性输出:** 通过状态机控制 Agent 的流转，避免了传统对话式 AI 的随机性。

## 使用场景
- 企业内部新技术预研。
- 开源项目的自动化文档维护。
- 技术博主的创作辅助工具。
