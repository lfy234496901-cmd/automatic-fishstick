from langgraph.graph import StateGraph, END
from agents import TechStreamAgents, AgentState

def create_workflow():
    agents = TechStreamAgents()
    workflow = StateGraph(AgentState)

    # 添加节点
    workflow.add_node("research", agents.researcher)
    workflow.add_node("analyze_code", agents.code_analyst)
    workflow.add_node("critic", agents.critic)
    workflow.add_node("write", agents.writer)

    # 构建边缘逻辑
    workflow.set_entry_point("research")
    workflow.add_edge("research", "analyze_code")
    workflow.add_edge("analyze_code", "critic")

    # 循环逻辑：如果评审未通过，则返回研究节点（体现长链推理）
    workflow.add_conditional_edges(
        "critic",
        lambda x: "research" if x["critique"] != "PASSED" and x["revision_count"] < 3 else "write"
    )
    workflow.add_edge("write", END)

    return workflow.compile()

if __name__ == "__main__":
    app = create_workflow()
    initial_state = {
        "topic": "大规模语言模型的分布式推理加速技术",
        "revision_count": 0
    }
    result = app.invoke(initial_state)
    print("\n--- 项目成果展示 ---")
    print(result["final_report"])
