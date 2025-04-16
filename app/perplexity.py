import requests
from app.config import PERPLEXITY_API_KEY

class PerplexityClient:
    def __init__(self, api_key=PERPLEXITY_API_KEY):
        self.api_key = api_key
        self.url = "https://api.perplexity.ai/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_response(self, messages, model="sonar", max_tokens=1000):
        """
        Generate a response using Perplexity AI API
        
        Args:
            messages (list): List of message objects (each with 'role' and 'content' keys)
            model (str): Model name (default: 'sonar')
            max_tokens (int): Maximum number of tokens to generate
            
        Returns:
            dict: Response from Perplexity AI
        """
        payload = {
            "temperature": 0.2,
            "top_p": 0.9,
            "return_images": False,
            "return_related_questions": False,
            "top_k": 0,
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 1,
            "web_search_options": {"search_context_size": "low"},
            "model": model,
            "max_tokens": max_tokens,
            "messages": messages
        }
        
        try:
            response = requests.post(self.url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error calling Perplexity API: {e}")
            return {"error": str(e)}
    
    def ask(self, query, system_prompt=None):
        """
        Simple helper method to ask a single question
        
        Args:
            query (str): User's question
            system_prompt (str, optional): System prompt to set context
            
        Returns:
            str: Generated text response
        """
        messages = []
        
        # Add system prompt if provided
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        # Add user query
        messages.append({"role": "user", "content": query})
        
        # Get response
        response = self.generate_response(messages)
        
        if "error" in response:
            return f"Sorry, I encountered an error: {response['error']}"
        
        try:
            return response["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            print(f"Error processing response: {e}")
            return "Sorry, I couldn't generate a response at this time."