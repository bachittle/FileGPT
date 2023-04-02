import openai
import os
from typing import List

def get_openai_response(model_name:str, messages:List[dict]):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
        stream=True
    )
    return response
