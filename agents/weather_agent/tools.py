from agents.weather_agent.prompt import WEATHER_TOOL_DESCRIPTION
from langchain.tools import tool
from langgraph.prebuilt import ToolNode
import requests


# Get the latitude and longitude of a city
def get_lat_and_long(city: str) -> tuple[float, float]:
    base_url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {"name": city, "count": 1, "language": "en", "format": "json"}

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    return (data["results"][0]["latitude"], data["results"][0]["longitude"])


# Define the weather tool
@tool("get_weather", description=WEATHER_TOOL_DESCRIPTION)
def get_weather(
    city: str,
    start_date: str,
    end_date: str,
) -> dict:
    latitude, longitude = get_lat_and_long(city)
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "hourly": ["temperature_2m", "rain", "snowfall"],
        "current": ["temperature_2m", "rain", "snowfall"],
        "start_date": start_date,
        "end_date": end_date,
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    hourly_data = {
        time: {
            "temperature_2m": temperature_2m,
            "rain": rain,
            "snowfall": snowfall,
        }
        for time, temperature_2m, rain, snowfall in zip(
            data["hourly"]["time"],
            data["hourly"]["temperature_2m"],
            data["hourly"]["rain"],
            data["hourly"]["snowfall"],
        )
    }
    del data["hourly"]
    data["hourly_data"] = hourly_data
    return data


tools = [get_weather]
tool_node = ToolNode(tools)
