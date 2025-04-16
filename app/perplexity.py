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
    
    def generate_response(self, messages, model="sonar", max_tokens=500):
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
    
    def markdown_to_plain_text(self, markdown_text):
        """
        Convert Markdown text to plain text by removing or replacing formatting.
        
        Args:
            markdown_text (str): Text in Markdown format
            
        Returns:
            str: Plain text with Markdown formatting removed or replaced
        """
        if not markdown_text:
            return ""
        
        # Replace bold (**text** or __text__) with just the text
        import re
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', markdown_text)
        text = re.sub(r'__(.*?)__', r'\1', text)
        
        # Replace italic (*text* or _text_) with just the text
        text = re.sub(r'\*(.*?)\*', r'\1', text)
        text = re.sub(r'_(.*?)_', r'\1', text)
        
        # Replace headers (# Header) with 'Header:'
        text = re.sub(r'^#\s+(.*)', r'\1:', text, flags=re.MULTILINE)
        text = re.sub(r'^##\s+(.*)', r'\1:', text, flags=re.MULTILINE)
        text = re.sub(r'^###\s+(.*)', r'\1:', text, flags=re.MULTILINE)
        
        # Replace bullet points with '- '
        text = re.sub(r'^\s*[-*+]\s+', '- ', text, flags=re.MULTILINE)
        
        # Replace numbered lists with '1. ', '2. ', etc.
        lines = text.split('\n')
        new_lines = []
        number = 0
        for line in lines:
            if re.match(r'^\s*\d+\.\s+', line):
                number += 1
                line = re.sub(r'^\s*\d+\.\s+', f'{number}. ', line)
            elif re.match(r'^\s*[-*+]\s+', line):
                number = 0  # Reset counter when switching to bullets
            new_lines.append(line)
        text = '\n'.join(new_lines)
        
        # Replace links with text (URL)
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1 (\2)', text)
        
        # Remove citations like [1], [2], etc.
        text = re.sub(r'\[\d+\]', '', text)
        
        # Replace code blocks and inline code with just the text
        text = re.sub(r'```.*?\n(.*?)\n```', r'\1', text, flags=re.DOTALL)
        text = re.sub(r'`(.*?)`', r'\1', text)
        
        # Replace blockquotes with '> '
        text = re.sub(r'^>\s+', '> ', text, flags=re.MULTILINE)
        
        # Replace multiple newlines with double newline for readability
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
        
        return text.strip()
    
    def ask(self, query, system_prompt=None):
        """
        Simple helper method to ask a single question
        
        Args:
            query (str): User's question
            system_prompt (str, optional): System prompt to set context
            
        Returns:
            str: Generated text response formatted for LINE
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
            # Convert Markdown response to plain text for LINE compatibility
            markdown_content = response["choices"][0]["message"]["content"]
            return self.markdown_to_plain_text(markdown_content)
        except (KeyError, IndexError) as e:
            print(f"Error processing response: {e}")
            return "Sorry, I couldn't generate a response at this time."