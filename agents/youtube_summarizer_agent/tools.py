from langgraph.prebuilt.tool_node import ToolNode
from langchain.tools import tool
from youtube_transcript_api import YouTubeTranscriptApi

from agents.youtube_summarizer_agent.prompt import YOUTUBE_TRANSCRIPT_TOOL_DESCRIPTION


# Tool to get the transcript of a YouTube video
@tool("get_youtube_video_transcript", description=YOUTUBE_TRANSCRIPT_TOOL_DESCRIPTION)
def get_youtube_video_transcript(video_id: str) -> list[dict]:
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)
    transcript = [
        {"start": snippet.start, "duration": snippet.duration, "text": snippet.text}
        for snippet in fetched_transcript
    ]
    return transcript


tools = [get_youtube_video_transcript]
tool_node = ToolNode(tools)
