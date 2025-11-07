# Search Agent 🔍

An intelligent web search agent built with LangGraph v1 that helps you find accurate, relevant, and up-to-date information from the web. The agent uses a **ReAct** (Reasoning + Acting) pattern with powerful search tools (DuckDuckGo and Tavily) to retrieve real-time information and provide comprehensive, well-sourced answers.

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- An API key from your chosen LLM provider (Anthropic, OpenAI, Google, etc.)
- A Tavily API key (for enhanced search capabilities) - [Get one here](https://tavily.com)

### Installation

> **Important**: Run all commands from the **project root directory** (`awesome-ai-agents/`).

1. **Create a `.env` file** at the project root and add your configuration:

```env
MODEL_NAME=claude-haiku-4-5
API_KEY=your-anthropic-api-key-here
TAVILY_API_KEY=your-tavily-api-key-here
```

> **Flexible Model Selection**: You can use **any LLM model and provider** you prefer:
>
> - **Anthropic**: `claude-sonnet-4-5`, `claude-haiku-4-5`
> - **OpenAI**: `gpt-4o-mini`, `gpt-5`, `gpt-4.1`
> - **Google**: `gemini-2.5-flash`, `gemini-2.5-pro`
> - **And more**: Any model supported by LangChain
>
> Just ensure the langchain library is installed and set the `MODEL_NAME` to your chosen model and `API_KEY` to your provider's API key.

2. **Install dependencies**:

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

3. **Run the agent**:

```bash
langgraph dev
```

The server will start on `http://127.0.0.1:2024`

> **Note**: Make sure you're in the project root directory when running this command.

## 💬 Usage

### Accessing the Agent

You can interact with the agent through:

1. **Langchain's Agent Chat UI**: [https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=search_agent](https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=search_agent)
2. **LangGraph's Studio UI**: [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)

### Example Queries

Try asking the agent questions like:

- "What are the latest developments in AI technology?"
- "What are today's top technology news stories?"

## 📁 Project Structure

```
agents/search_agent/
├── graph.py          # LangGraph workflow definition
├── nodes.py          # Node implementations (LLM calls)
├── model.py          # LLM model configuration
├── tools.py          # Search tools (DuckDuckGo & Tavily)
├── prompt.py         # System prompts and tool descriptions
└── README.md         # This file
```

---

## ✨ Features

- **Dual Search Engines**: Uses both DuckDuckGo (privacy-focused) and Tavily (AI-optimized) for comprehensive results
- **Smart Search Strategy**: Automatically selects the best search tool based on query type
- **Topic-Specific Search**: Filter results by topic (general, news, finance)
- **Domain Filtering**: Search within specific trusted domains
- **Source Citations**: Always provides URLs and sources for information
- **Real-Time Information**: Fetches current, up-to-date data from the web
- **Comprehensive Answers**: Synthesizes information from multiple sources into clear, well-structured responses

## 🏗️ Architecture

This agent implements the **ReAct (Reasoning + Acting)** pattern:

1. **Reasoning**: The LLM analyzes the user's query and determines the best search strategy
2. **Acting**: Calls appropriate search tools (DuckDuckGo or Tavily) to fetch information
3. **Processing**: Analyzes and filters search results for relevance
4. **Synthesizing**: Combines information from multiple sources
5. **Responding**: Delivers a comprehensive, well-cited answer with source URLs

---

## 🔧 How It Works

### 1. User Input

The user asks a question or requests information on any topic.

### 2. Query Analysis

The LLM analyzes the query to determine:

- What type of information is needed (general, news, finance)
- Which search tool(s) would be most effective
- Whether domain-specific search is beneficial
- How many results are needed for comprehensive coverage

### 3. Search Execution

The agent has two powerful search tools:

#### **DuckDuckGo Search**

- Privacy-focused general web search
- Best for: tutorials, documentation, general queries
- Returns: titles, snippets, links, sources

#### **Tavily Search**

- AI-optimized search with advanced filtering
- Best for: research, current events, finance, domain-specific searches
- Features: topic filtering, domain inclusion, relevance scoring
- Returns: detailed content, URLs, relevance scores, publication dates

### 4. Information Synthesis

The LLM processes search results to:

- Extract relevant information
- Cross-reference multiple sources
- Filter out irrelevant or low-quality results
- Organize information logically
- Identify key facts and important details

### 5. Response Generation

The agent creates a comprehensive answer that:

- Starts with a direct answer to the question
- Provides detailed information organized with clear formatting
- Cites all sources with URLs
- Includes relevant context and background
- Presents multiple perspectives when appropriate

## 🛠️ API Details

### DuckDuckGo Search Tool

```python
duck_duck_go_search(
    query: str,           # Search query
    max_results: int = 5  # Maximum number of results (default: 5)
)
```

**Returns:**

```python
[
    {
        "title": "Result title",
        "snippet": "Brief description",
        "link": "https://example.com",
        "source": "example.com"
    },
    # ... more results
]
```

### Tavily Search Tool

```python
tavily_search(
    query: str,                              # Search query
    topic: Literal["general", "news", "finance"] = "general",
    include_domains: list[str] = None,       # Filter by specific domains
    max_results: int = 5                     # Maximum number of results
)
```

**Returns:**

```python
[
    {
        "title": "Result title",
        "content": "Detailed content optimized for AI",
        "url": "https://example.com",
        "score": 0.95,                       # Relevance score (0.0 to 1.0)
        "raw_content": None                   # Raw HTML content when available
    },
    # ... more results
]
```

## 🌐 External APIs Used

- **[DuckDuckGo Search](https://duckduckgo.com)**: Privacy-focused search engine (no API key required)
- **[Tavily AI Search](https://tavily.com)**: AI-optimized search API designed for LLM applications (API key required)

### Search Capabilities

#### DuckDuckGo

- ✅ No API key required
- ✅ Privacy-focused
- ✅ Fast general web search
- ❌ No advanced filtering options

#### Tavily

- ✅ AI-optimized results
- ✅ Topic filtering (news, finance)
- ✅ Domain-specific search
- ✅ Relevance scoring
- ✅ Publication dates
- ⚠️ Requires API key

### Limitations

- Search results depend on what's publicly available on the web
- Some content may be behind paywalls or require authentication
- Result quality varies by search engine and query
- Rate limits may apply (especially for Tavily API)
- Real-time data availability depends on source freshness

## 📚 Learn More

- [LangGraph v1 Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Tavily AI Documentation](https://docs.tavily.com)
- [DuckDuckGo Search](https://duckduckgo.com)
