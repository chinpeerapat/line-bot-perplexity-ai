from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)
from app.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET, PERPLEXITY_SYSTEM_PROMPT
from app.perplexity import PerplexityClient

# Initialize LINE API client
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Initialize Perplexity client
pplx_client = PerplexityClient()

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    """
    Handle text messages from LINE users
    
    Args:
        event: LINE message event
    """
    try:
        user_message = event.message.text
        print(f"Received message: {user_message}")
        
        # Generate response using Perplexity AI
        ai_response = pplx_client.ask(user_message, system_prompt=PERPLEXITY_SYSTEM_PROMPT)
        
        # Reply to the user
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=ai_response)
        )
    except Exception as e:
        print(f"Error processing message: {e}")
        # Send error message to user
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Sorry, I encountered an error while processing your request.")
        )