# Import necessary modules
import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

class TestLineBot(unittest.TestCase):
    def test_root_endpoint(self):
        """Test the root endpoint returns successful response"""
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "status": "OK", 
            "message": "LINE Bot with Perplexity AI Integration is running"
        })

    @patch('app.line_handler.handler')
    def test_webhook_invalid_signature(self, mock_handler):
        """Test webhook with invalid signature"""
        mock_handler.handle.side_effect = Exception("Invalid signature")
        
        response = client.post(
            "/webhook",
            headers={"X-Line-Signature": "invalid_signature"},
            json={"events": []}
        )
        
        self.assertEqual(response.status_code, 500)

if __name__ == "__main__":
    unittest.main()