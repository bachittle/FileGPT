PERSONALITIES = [
    "python_coder",
]

MAP_PERSONALITY_TO_OPENAI = {
    "python_coder": """
You only give your responses with python code.    
When you need to tell the user something, use code comments.

Example:
User: What is your name?
Bot: # My name is GPT-3
User: Write some code to print your name
Bot: print("GPT-3")
"""
}

def get_personality(personality: str) -> str:
    if personality in PERSONALITIES:
        return personality
    else:
        print(f"Personality {personality} not found. Available personalities: {', '.join(PERSONALITIES)}")
        return None 