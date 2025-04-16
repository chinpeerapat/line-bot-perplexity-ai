import os
from dotenv import load_dotenv

# Try to load environment variables from .env file
load_dotenv()

# LINE Bot credentials
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "your_line_channel_secret")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "your_line_channel_access_token")

# Perplexity AI credentials
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "your_perplexity_api_key")

# App settings
PORT = int(os.getenv("PORT", 8000))