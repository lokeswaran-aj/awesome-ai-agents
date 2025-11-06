# Weather Analyst Agent 🌤️

An intelligent weather analysis agent built with LangGraph v1 that provides detailed weather forecasts for any city worldwide. The agent uses a ReAct (Reasoning + Acting) pattern to understand user queries and fetch real-time weather data from the Open-Meteo API.

![weather-agent-demo](https://github.com/user-attachments/assets/f6ba0a19-0ed1-477c-b85b-0c67dbbdf80c)


## ✨ Features

- **Natural Language Queries**: Ask about weather in conversational language
- **Flexible Date Ranges**: Get weather forecasts for specific date ranges
- **Detailed Metrics**: Temperature, rainfall, and snowfall data
- **Geocoding Support**: Automatically converts city names to coordinates
- **Hourly Forecasts**: Detailed hour-by-hour weather breakdown
- **ReAct Pattern**: Combines reasoning and action for intelligent responses

## 🏗️ Architecture

This agent implements the **ReAct (Reasoning + Acting)** pattern:

1. **Reasoning**: The LLM analyzes the user's query and decides what information is needed
2. **Acting**: Calls the weather tool with appropriate parameters (city, date range)
3. **Responding**: Synthesizes the weather data into a natural language response

### What is ReAct?

ReAct agents combine reasoning and action in an interleaved manner. The agent:

- **Thinks** about what to do next
- **Acts** by calling tools/functions
- **Observes** the results
- **Repeats** until the task is complete

## 📁 Project Structure

```
agents/weather_agent/
├── graph.py          # LangGraph workflow definition
├── nodes.py          # Node implementations (LLM calls)
├── model.py          # LLM model configuration
├── tools.py          # Weather tool and API integration
├── prompt.py         # System prompts and tool descriptions
└── README.md         # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- An API key from your chosen LLM provider (Anthropic, OpenAI, Google, etc.)

### Installation

> **Important**: Run all commands from the **project root directory** (`awesome-ai-agents/`).

1. **Create a `.env` file** at the project root and add your configuration:

```env
MODEL_NAME=claude-haiku-4-5
API_KEY=your-anthropic-api-key-here
```

> **Flexible Model Selection**: You can use **any LLM model and provider** you prefer:
>
> - **Anthropic**: `claude-sonnet-4-5`, `claude-haiku-4-5`
> - **OpenAI**: `gpt-4o-mini`, `gpt-5`, `gpt-4.1`
> - **Google**: `gemini-2.5-flash`, `gemini-2.5-pro`
> - **And more**: Any model supported by LangChain
>
> Just ensure the langchain library is installed and set the `MODEL_NAME` to your chosen model and `API_KEY` to your provider's API key.

1. **Install dependencies**:

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

1. **Langchain's Agent Chat UI**: [https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=weather_agent](https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=weather_agent)
2. **LangGraph's Studio UI**: [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)

### Example Queries

Try asking the agent questions like:

- "How is the weather in Bangalore this weekend?"
- "Will it rain in London next week?"
- "Give me the temperature forecast for Tokyo from 2025-11-15 to 2025-11-20"
- "What's the weather looking like in San Francisco for the next 5 days?"

## 🔧 How It Works

### 1. User Query

The user asks a weather-related question in natural language.

### 2. LLM Processing

The LLM model analyzes the query and determines:

- Which city the user is asking about
- What date range is needed
- What specific weather information to fetch

### 3. Tool Execution

The `get_weather` tool:

1. Converts the city name to coordinates using geocoding
2. Calls the Open-Meteo API with the appropriate parameters
3. Returns structured weather data

### 4. Response Generation

The LLM synthesizes the weather data into a natural, conversational response.

## 🛠️ API Details

### Weather Tool Parameters

```python
get_weather(
    city: str,          # City name (e.g., "Bangalore", "London")
    start_date: str,    # Start date in YYYY-MM-DD format
    end_date: str       # End date in YYYY-MM-DD format
)
```

### Data Returned

- **Current conditions**: Temperature, rain, snowfall
- **Hourly forecast**: Hour-by-hour breakdown for the date range
- **Metadata**: Latitude, longitude, timezone, elevation

## 🌐 External APIs Used

- **[Open-Meteo API](https://open-meteo.com/)**: Free weather forecast API (no API key required)
- **[Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)**: Converts city names to coordinates

## 📚 Learn More

- [LangGraph v1 Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Open-Meteo API Docs](https://open-meteo.com/en/docs)
