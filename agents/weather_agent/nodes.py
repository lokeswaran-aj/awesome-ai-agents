from langchain.agents import AgentState
from langchain.messages import SystemMessage
from datetime import datetime
from agents.weather_agent.model import model
from agents.weather_agent.tools import tools
from agents.weather_agent.prompt import WEATHER_AGENT_SYSTEM_PROMPT

# Bind the tools to the model
model_with_tools = model.bind_tools(tools)


def call_llm(state: AgentState) -> AgentState:
    """Call the LLM with the system prompt and the messages"""
    system_prompt = SystemMessage(
        WEATHER_AGENT_SYSTEM_PROMPT.format(
            current_date_time=datetime.now().strftime(
                "%A, %Y-%m-%d %H:%M:%S"
            )  # Current day, date and time
        )
    )
    response = model_with_tools.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}
