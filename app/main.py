from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from app.config import LINE_CHANNEL_SECRET
from app.line_handler import handler
from linebot.v3.exceptions import InvalidSignatureError
import uvicorn

app = FastAPI(title="LINE Bot with Perplexity AI Integration")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "OK", "message": "LINE Bot with Perplexity AI Integration is running"}

@app.post("/webhook")
async def line_webhook(request: Request):
    """
    LINE Webhook endpoint
    
    This endpoint receives events from LINE and processes them
    """
    # Get X-Line-Signature header and request body
    signature = request.headers.get("X-Line-Signature", "")
    body = await request.body()
    body_text = body.decode("utf-8")
    
    print(f"Received webhook event\nSignature: {signature}\nBody: {body_text}")
    
    try:
        # Handle the webhook event using the LINE handler
        handler.handle(body_text, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception as e:
        print(f"Error handling webhook: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    
    return JSONResponse(content={"status": "OK"}, status_code=200)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)