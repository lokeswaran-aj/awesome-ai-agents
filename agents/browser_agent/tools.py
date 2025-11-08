from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import ToolNode
import os
import asyncio

PLAYWRIGHT_MCP_EXTENSION_TOKEN = os.getenv("PLAYWRIGHT_MCP_EXTENSION_TOKEN")

client = MultiServerMCPClient(
    {
        "browser": {
            "transport": "stdio",
            "command": "npx",
            "args": ["@playwright/mcp@latest", "--extension"],
            "env": {"PLAYWRIGHT_MCP_EXTENSION_TOKEN": PLAYWRIGHT_MCP_EXTENSION_TOKEN},
        }
    }
)

# Global variables
tools = None
tool_node = None
_session_task = None
_init_event = None


async def _keep_session_alive():
    """Background task to keep MCP session alive"""
    global tools, tool_node, _init_event

    async with client.session("browser") as session:
        tools = await load_mcp_tools(session)
        tool_node = ToolNode(tools)
        _init_event.set()  # Signal that tools are ready

        # Keep session alive indefinitely
        await asyncio.Event().wait()


async def initialize_tools():
    """Initialize tools with persistent session"""
    global _session_task, _init_event

    if _session_task is None:
        _init_event = asyncio.Event()
        _session_task = asyncio.create_task(_keep_session_alive())

    # Wait for initialization to complete
    await _init_event.wait()
    return tools
