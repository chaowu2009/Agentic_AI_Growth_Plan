import urllib.request
import os
import json
from typing import List
from AgentClass import Message
from pydantic import BaseModel

class LLMClient:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model = model_name
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/chat/completions"
    
    def __call__(self, messages: List[Message], temperature: float = 0.2) -> str:
        """Invokes the LLM via HTTP POST."""
        payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "temperature": temperature,
            "max_tokens": 1000
        }
        
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            self.api_url, 
            data=data, 
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error calling LLM: {str(e)}"