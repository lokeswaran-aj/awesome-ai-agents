from langchain.agents import AgentState
from langchain.messages import SystemMessage
from agents.youtube_summarizer_agent.model import model
from agents.youtube_summarizer_agent.tools import tools
from agents.youtube_summarizer_agent.prompt import (
    YOUTUBE_VIDEO_SUMMARIZER_SYSTEM_PROMPT,
)

# Bind the tools to the model
model_with_tools = model.bind_tools(tools)


def call_llm(state: AgentState) -> AgentState:
    """Call the LLM with the system prompt and the messages"""
    system_prompt = SystemMessage(YOUTUBE_VIDEO_SUMMARIZER_SYSTEM_PROMPT)
    response = model_with_tools.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}
