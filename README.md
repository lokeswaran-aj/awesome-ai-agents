# Awesome AI Agents 🤖

A curated collection of open-source AI agents built with LangGraph v1 for learning and experimentation. Each agent demonstrates different patterns, capabilities, and use cases in AI agent development.

## 📚 Agent Collection

| Agent                                                             | Description                                                                         | Pattern | Status      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------- | ----------- |
| [Weather Analyst](./agents/weather_agent/README.md)               | Intelligent weather analyst agent that provides detailed weather data for any city  | ReAct   | ✅ Complete |
| [YouTube Summarizer](./agents/youtube_summarizer_agent/README.md) | Smart video summarization agent that converts YouTube videos into concise summaries | ReAct   | ✅ Complete |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- API key from your chosen LLM provider (Anthropic, OpenAI, Google, etc.)

### Setup

1. **Clone the repository**:

```bash
git clone https://github.com/lokeswaran-aj/awesome-ai-agents.git
cd awesome-ai-agents
```

2. **Copy the `.env.example` file to `.env` and add the secrets for the agents you want to use**:

```env
MODEL_NAME=claude-haiku-4-5
API_KEY=your-anthropic-api-key-here
```

3. **Install dependencies**:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

4. **Run an agent**:

```bash
langgraph dev
```

The server will start on `http://127.0.0.1:2024`

## 💬 Usage

### Accessing the Agents

You can interact with the agents through:

1. **Langchain's Agent Chat UI**:

   - Weather Agent: [https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=weather_agent](https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=weather_agent)
   - YouTube Summarizer: [https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=youtube_summarizer_agent](https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=youtube_summarizer_agent)

2. **LangGraph's Studio UI**: [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)

---

## 🏗️ Project Structure

```
awesome-ai-agents/
├── agents/                      # Agent implementations
│   ├── weather_agent/           # Weather analyst agent
│   │   ├── graph.py             # LangGraph workflow
│   │   ├── nodes.py             # Node implementations
│   │   ├── tools.py             # Tool definitions
│   │   ├── model.py             # LLM configuration
│   │   ├── prompt.py            # System prompts
│   │   └── README.md            # Agent documentation
│   └── youtube_summarizer_agent/ # YouTube summarizer agent
│       ├── graph.py             # LangGraph workflow
│       ├── nodes.py             # Node implementations
│       ├── tools.py             # Tool definitions
│       ├── model.py             # LLM configuration
│       ├── prompt.py            # System prompts
│       └── README.md            # Agent documentation
├── langgraph.json               # Centralized LangGraph configuration
├── .env.example                 # Example environment variables
├── pyproject.toml               # Project dependencies
└── README.md                    # This file
```

## 💡 Agent Usage

Each agent has its own README with:

- Detailed description and use cases
- Setup instructions
- Example queries
- Architecture explanation
- API documentation

Click on any agent in the table above to learn more!

## 🛠️ Tech Stack

- **[LangGraph v1](https://docs.langchain.com/oss/python/langgraph/overview)**: Framework for building stateful, multi-agent applications
- **[LangChain v1](https://docs.langchain.com/oss/python/langchain/overview)**: Tools and integrations for LLM applications
- **Python 3.13+**: Modern Python with latest features
- **[uv](https://github.com/astral-sh/uv)**: Fast Python package installer and resolver

---

## 🤝 Contributing

This is a learning project! Feel free to:

- Add new agents with different patterns
- Improve existing agents
- Raise issue for the agents you want to see

## 📝 License

MIT License - feel free to use these agents in your own projects!

---

⭐ **Star this repo** if you find it helpful for learning about AI agents!
