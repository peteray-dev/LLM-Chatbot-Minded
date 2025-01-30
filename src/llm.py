# import os
# import openai
from src.prompt import system_instruction
from openai import OpenAI

client = OpenAI()

messages = [
    {"role":"system", "content": system_instruction}
]

def ask_order(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature
    )
    return response.choices[0].message.content



# Hugging face, one can train the model on hugging face autotrain using some financial dataset
# import requests

# messages = [
#     {'role': 'system', 'content': system_instruction}
# ]
# # Hugging Face API URL
# API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"

# # Replace with your Hugging Face API key


# def ask_order(messages):
#     """
#     Generate a response using Hugging Face's inference API.
#     """
#     # ✅ Ensure the prompt format is structured correctly
#     prompt = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])  
#     prompt += "\nAssistant:"  # Ensure the model knows it's time to generate a response.

#     # Payload with temperature tuning
#     payload = {
#         "inputs": prompt,
#         "parameters": {"max_new_tokens": 200, "temperature": 0.3}  # Adjust temperature for response control
#     }

#     # Send request to Hugging Face API
#     response = requests.post(API_URL, headers=HEADERS, json=payload)

#     if response.status_code == 200:
#         return response.json()[0]["generated_text"].split("Assistant:")[-1].strip()  # ✅ Extract only AI response
#     else:
#         return f"Error: {response.json()}"
