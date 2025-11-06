# Youtube Summarizer Agent 📺

An intelligent YouTube video summarization agent built with LangGraph v1 that converts lengthy videos into concise, easy-to-digest summaries. The agent uses a **ReAct** (Reasoning + Acting) pattern by using the `get_youtube_video_transcript` tool to fetch video transcripts and use the LLM to summarize them while filtering out promotional content and filler.

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

1. **Langchain's Agent Chat UI**: [https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=youtube_summarizer_agent](https://agentchat.vercel.app/?apiUrl=http://localhost:2024&assistantId=youtube_summarizer_agent)
2. **LangGraph's Studio UI**: [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)

### Example Queries

Try asking the agent questions like:

- "Summarize this video: https://www.youtube.com/watch?v=eJXVEju3XLM"
- "Summarize this in bullet points: https://youtu.be/lraHlXpuhKs?si=8FghXJlG3P-fddUK"

## 📁 Project Structure

```
agents/youtube_summarizer_agent/
├── graph.py          # LangGraph workflow definition
├── nodes.py          # Node implementations (LLM calls)
├── model.py          # LLM model configuration
├── tools.py          # YouTube transcript tool
├── prompt.py         # System prompts and tool descriptions
└── README.md         # This file
```

---

## ✨ Features

- **Flexible Summary Formats**: Automatically chooses the best format (paragraph, bullet points, hierarchical, mindmap-style) based on video content
- **Smart Content Filtering**: Removes sponsors, like/subscribe prompts, and other YouTube filler
- **Multiple Content Types**: Adapts to tutorials, interviews, lectures, and more
- **Natural Language Input**: Simply provide a YouTube URL and get a summary
- **Time-Saving**: Get the key points without watching the entire video

## 🏗️ Architecture

This agent implements the **ReAct (Reasoning + Acting)** pattern:

1. **Reasoning**: The LLM analyzes the user's request and extracts the video ID from the URL
2. **Acting**: Calls the transcript tool to fetch the video's complete transcript
3. **Processing**: Filters out promotional content and filler
4. **Synthesizing**: Creates a concise summary in the most appropriate format
5. **Responding**: Delivers the summary focused on key points and main ideas

---

## 🔧 How It Works

### 1. User Input

The user provides a YouTube URL and optionally specifies the desired summary format.

### 2. Video ID Extraction

The LLM extracts the video ID from the URL (supports both `youtube.com/watch?v=` and `youtu.be/` formats).

### 3. Transcript Retrieval

The `get_youtube_video_transcript` tool:

1. Takes the video ID as input
2. Fetches the complete transcript using YouTube's caption/subtitle data
3. Returns timestamped transcript segments with start time, duration, and text

### 4. Content Analysis

The LLM analyzes the transcript to:

- Identify the main topic and key themes
- Filter out promotional content, sponsors, and filler
- Recognize the video type (tutorial, interview, lecture, etc.)
- Determine the optimal summary format

### 5. Summary Generation

The agent creates a concise summary that:

- Captures the essence of the video
- Preserves important details, examples, and quotes
- Uses the most appropriate format for the content
- Focuses on time-saving and information retention

## 🛠️ API Details

### Transcript Tool Parameters

```python
get_youtube_video_transcript(
    video_id: str  # YouTube video ID (e.g., "dQw4w9WgXcQ")
)
```

### Data Returned

```python
[
    {
        "start": 0.0,          # Timestamp in seconds
        "duration": 2.5,       # Duration of this segment
        "text": "Hello and..."  # Transcript text
    },
    # ... more segments
]
```

## 🌐 External APIs Used

- **[YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)**: Python library to fetch YouTube video transcripts/captions (no API key required)

### Limitations

- Only works with videos that have captions/transcripts available
- Cannot summarize videos without transcripts (live streams without captions, very new videos, etc.)
- Transcript quality depends on YouTube's automatic or manual captioning

## 📚 Learn More

- [LangGraph v1 Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
