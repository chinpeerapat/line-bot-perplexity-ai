import uvicorn
from app.config import PORT

if __name__ == "__main__":
    print(f"Starting LINE Bot with Perplexity AI Integration on port {PORT}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)