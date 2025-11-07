from langchain.agents import AgentState
from langchain.messages import SystemMessage
from agents.search_agent.model import model
from agents.search_agent.tools import tools
from agents.search_agent.prompt import (
    SEARCH_AGENT_SYSTEM_PROMPT,
)
from datetime import datetime

# Bind the tools to the model
model_with_tools = model.bind_tools(tools)


def call_llm(state: AgentState) -> AgentState:
    """Call the LLM with the system prompt and the messages"""
    system_prompt = SystemMessage(
        SEARCH_AGENT_SYSTEM_PROMPT.format(
            current_date_time=datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
        )
    )
    response = model_with_tools.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}
