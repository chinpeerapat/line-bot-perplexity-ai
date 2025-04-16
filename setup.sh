#!/bin/bash

# Exit on any error
set -e

echo "===== LINE Bot with Perplexity AI Integration ====="
echo "Setting up the project..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment 
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Prompt for configuration if .env doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file for configuration..."
    
    echo "Enter your LINE Channel Secret:"
    read line_secret
    
    echo "Enter your LINE Channel Access Token:"
    read line_token
    
    echo "Enter your Perplexity AI API Key:"
    read pplx_key
    
    echo "Enter port to run the server on (default: 8000):"
    read port
    port=${port:-8000}
    
    # Create .env file
    cat > .env << EOF
LINE_CHANNEL_SECRET=$line_secret
LINE_CHANNEL_ACCESS_TOKEN=$line_token
PERPLEXITY_API_KEY=$pplx_key
PORT=$port
EOF
    
    echo ".env file created successfully!"
fi

echo "Setup complete! Run the bot with: python run.py"