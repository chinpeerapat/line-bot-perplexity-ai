from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from app.config import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET, PERPLEXITY_SYSTEM_PROMPT, TRIGGER_PHRASE
from app.perplexity import PerplexityClient

# Initialize LINE Webhook handler and v3 API configuration
handler = WebhookHandler(LINE_CHANNEL_SECRET)
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

# Initialize Perplexity client
pplx_client = PerplexityClient()

@handler.add(MessageEvent, message=TextMessageContent)
def handle_text_message(event):
    """
    Handle text messages from LINE users
    
    Args:
        event: LINE message event
    """
    try:
        raw_text = event.message.text.strip()
        print(f"Received message: {raw_text}")
        # In group or room chats, only proceed if message starts with trigger phrase
        if event.source.type in ["group", "room"]:
            if not raw_text.startswith(TRIGGER_PHRASE):
                return  # not a command for the bot
            # strip trigger phrase
            raw_text = raw_text[len(TRIGGER_PHRASE):].strip()
        # Generate response using Perplexity AI
        ai_response = pplx_client.ask(raw_text, system_prompt=PERPLEXITY_SYSTEM_PROMPT)
        
        # Reply to the user using v3 client
        with ApiClient(configuration) as api_client:
            messaging_api = MessagingApi(api_client)
            messaging_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=ai_response)]
                )
            )
    except Exception as e:
        print(f"Error processing message: {e}")
        # Send error message to user using v3 client
        with ApiClient(configuration) as api_client:
            messaging_api = MessagingApi(api_client)
            messaging_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Sorry, I encountered an error while processing your request.")]
                )
            )