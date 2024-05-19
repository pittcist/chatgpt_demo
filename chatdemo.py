from dotenv import load_dotenv, dotenv_values 
from openai import OpenAI
import os

# The api_key is stroed in a hidden environment file

# Loading variables from .env file
load_dotenv() 

# Getting the API key
api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)

client = OpenAI(api_key=api_key)

def call_chatgpt(prompt, model='gpt-3.5-turbo', max_tokens=50, temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    return response.choices[0].message.content

# Example usage
prompt = "Why did the chicken cross the road?"
response = call_chatgpt(prompt)
print(response)