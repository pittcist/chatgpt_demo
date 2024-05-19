from dotenv import load_dotenv, dotenv_values 
from openai import OpenAI
import os

# loading variables from .env file
load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)
#api_key is stroed in environment

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