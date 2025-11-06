from langgraph.prebuilt import tools_condition
from langgraph.graph import END, START
from langgraph.graph.state import StateGraph
from langchain.agents import AgentState

from agents.youtube_summarizer_agent.tools import tool_node
from agents.youtube_summarizer_agent.nodes import call_llm

# Build the graph
graph_builder = StateGraph(AgentState)

graph_builder.add_node("llm", call_llm)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "llm")

# Use prebuilt tools_condition to determine if the next node should be "tools" or END
graph_builder.add_conditional_edges(
    "llm",
    tools_condition,
    {"tools": "tools", "__end__": END},
)
graph_builder.add_edge("tools", "llm")
graph_builder.add_edge("llm", END)

# Compile the graph
graph = graph_builder.compile()
