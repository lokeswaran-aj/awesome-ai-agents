import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# Get the model name and API key from the environment variables
model_name = os.getenv("MODEL_NAME")

if not model_name:
    raise ValueError("MODEL_NAME is not set")

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY is not set")

model = init_chat_model(model_name, api_key=api_key)
