from langchain.messages import ToolMessage
from langgraph.prebuilt.tool_node import ToolNode
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.tools import ToolRuntime, tool
from langchain_tavily import TavilySearch
from typing import Literal

from langgraph.types import Command
from agents.search_agent.prompt import (
    DUCK_DUCK_GO_SEARCH_TOOL_DESCRIPTION,
    TAVILY_SEARCH_TOOL_DESCRIPTION,
)


@tool("duck_duck_go_search", description=DUCK_DUCK_GO_SEARCH_TOOL_DESCRIPTION)
def duck_duck_go_search(
    query: str,
    max_results: int = 5,
    runtime: ToolRuntime = None,
) -> list[dict] | Command:
    try:
        search = DuckDuckGoSearchResults(
            output_format="list",
            num_results=max_results,
        )
        results = search.invoke(query)
        return results
    except Exception as e:
        print(f"DuckDuckGo search error: {e}")
        # If runtime is available, return Command with error message
        return Command(
            update={
                "messages": [
                    ToolMessage(
                        content=f"Error: Failed to search the web using DuckDuckGo. {str(e)}",
                        tool_call_id=runtime.tool_call_id,
                    )
                ]
            }
        )


@tool("tavily_search", description=TAVILY_SEARCH_TOOL_DESCRIPTION)
def tavily_search(
    query: str,
    topic: Literal["general", "news", "finance"] = "general",
    include_domains: list[str] = None,
    max_results: int = 5,
    runtime: ToolRuntime = None,
) -> list[dict] | Command:
    try:
        search = TavilySearch(
            max_results=max_results,
            include_domains=include_domains,
            topic=topic,
        )
        response = search.invoke({"query": query})
        # Extract just the results list for consistency with duck_duck_go_search
        results = response.get("results", []) if isinstance(response, dict) else []
        return results
    except Exception as e:
        print(f"Tavily search error: {e}")
        # If runtime is available, return Command with error message
        return Command(
            update={
                "messages": [
                    ToolMessage(
                        content=f"Error: Failed to search the web using Tavily. {str(e)}",
                        tool_call_id=runtime.tool_call_id,
                    )
                ]
            }
        )


tools = [duck_duck_go_search, tavily_search]
tool_node = ToolNode(tools)
