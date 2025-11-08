from langchain.agents import AgentState
from langchain.messages import SystemMessage
from agents.browser_agent.model import model
from agents.browser_agent.tools import initialize_tools
from agents.browser_agent.prompt import (
    BROWSER_AGENT_SYSTEM_PROMPT,
)
from datetime import datetime


async def call_llm(state: AgentState) -> AgentState:
    """Call the LLM with the system prompt and the messages"""
    # Get tools with persistent session
    tools = await initialize_tools()
    model_with_tools = model.bind_tools(tools)

    system_prompt = SystemMessage(
        BROWSER_AGENT_SYSTEM_PROMPT.format(
            current_date_time=datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
        )
    )
    response = await model_with_tools.ainvoke([system_prompt] + state["messages"])
    return {"messages": [response]}
