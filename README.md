# LINE Bot with Perplexity AI Integration

[![GitHub license](https://img.shields.io/github/license/chinpeerapat/line-bot-perplexity-ai)](https://github.com/chinpeerapat/line-bot-perplexity-ai/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.1-green)](https://fastapi.tiangolo.com/)
[![LINE Bot SDK](https://img.shields.io/badge/LINE%20Bot%20SDK-3.5.0-brightgreen)](https://github.com/line/line-bot-sdk-python)

A LINE Bot built using FastAPI that integrates with the Perplexity AI API to provide intelligent responses to user messages.

## Features

- LINE Messaging API integration
- FastAPI web server
- Perplexity AI API for natural language processing
- Easy configuration via environment variables

## Prerequisites

- Python 3.7 or higher
- A LINE developer account and channel
- Perplexity AI API key

## Setup and Installation

1. **Clone the repository**

```bash
git clone https://github.com/chinpeerapat/line-bot-perplexity-ai.git
cd line-bot-perplexity-ai
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root with the following variables:

```bash
LINE_CHANNEL_SECRET=your_line_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
PERPLEXITY_API_KEY=your_perplexity_api_key
PORT=8000
PERPLEXITY_MODEL=sonar
PERPLEXITY_MAX_TOKENS=500
PERPLEXITY_SEARCH_CONTEXT_SIZE=low
PERPLEXITY_SYSTEM_PROMPT="You are a helpful assistant that provides accurate and useful information.\nPlease keep your answers concise and to the point, optimized for reading on a small screen."
```

5. **Run the application**

```bash
python run.py
```

## Development

### Project Structure

```
line-bot-perplexity-ai/
├── app/
│   ├── __init__.py
│   ├── config.py           # Configuration settings
│   ├── main.py             # FastAPI application
│   ├── line_handler.py     # LINE webhook event handler
│   └── perplexity.py       # Perplexity AI client
├── .env                    # Environment variables (create this file)
├── requirements.txt        # Dependencies
├── run.py                  # Application entry point
├── setup.sh                # Setup script
└── README.md               # Project documentation
```

## Deployment

### Local Deployment with ngrok

For testing, you can use ngrok to expose your local server to the internet:

1. Install ngrok: https://ngrok.com/download
2. Start your FastAPI server: `python run.py`
3. In a new terminal, run: `ngrok http 8000`
4. Copy the HTTPS URL from ngrok (e.g., https://xxxx-xx-xx-xxx-xx.ngrok.io)
5. Set this URL + "/webhook" as the Webhook URL in your LINE Channel settings

### Production Deployment

For production deployment, you can use services like:

- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Digital Ocean App Platform

Make sure to set the required environment variables in your deployment environment.

## LINE Bot Configuration

1. Go to the [LINE Developers Console](https://developers.line.biz/console/)
2. Create or select a provider
3. Create a new Channel (Messaging API)
4. Get your Channel Secret and Channel Access Token
5. Set the Webhook URL to your deployed application's URL + "/webhook"
6. Enable "Use webhook" option

## Perplexity AI Configuration

1. Go to [Perplexity AI](https://www.perplexity.ai/)
2. Sign up and get your API key
3. Set the following environment variables in your `.env` file:
   - `PERPLEXITY_API_KEY`
   - `PERPLEXITY_MODEL`
   - `PERPLEXITY_MAX_TOKENS`
   - `PERPLEXITY_SEARCH_CONTEXT_SIZE`
   - `PERPLEXITY_SYSTEM_PROMPT`

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.