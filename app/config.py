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

# Perplexity AI settings
PERPLEXITY_MODEL = os.getenv("PERPLEXITY_MODEL", "sonar")
PERPLEXITY_MAX_TOKENS = int(os.getenv("PERPLEXITY_MAX_TOKENS", 500))
PERPLEXITY_SEARCH_CONTEXT_SIZE = os.getenv("PERPLEXITY_SEARCH_CONTEXT_SIZE", "low")
PERPLEXITY_SYSTEM_PROMPT = os.getenv(
    "PERPLEXITY_SYSTEM_PROMPT",
    """You are a helpful assistant that provides accurate and useful information.
Please keep your answers concise and to the point, optimized for reading on a small screen."""
)

# Trigger phrase for group/room chats; only respond when message starts with this prefix
TRIGGER_PHRASE = os.getenv("TRIGGER_PHRASE", "/ask")