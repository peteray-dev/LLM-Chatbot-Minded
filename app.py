import chainlit as cl
from src.llm import ask_order, messages  

from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Welcome to **Minded** – Your AI Financial Assistant! 🚀\n\n"
                "💰 *Get smart insights on saving, spending & credit management.*\n"
                "📊 *Track expenses, monitor credit, & plan investments easily.*\n"
                "💡 *Ask me anything about your finances!*",
    ).send()

    
@cl.on_message
async def main(message: cl.Message):
    # Append user's message
    messages.append({'role': 'user', 'content': message.content})

    # Get AI response
    response = ask_order(messages)

    # Append AI response to message history
    messages.append({'role': 'assistant', 'content': response})

    # Send response back to the user
    await cl.Message(content=response).send()

# For huggingface model
# import chainlit as cl
# from src.llm import ask_order, messages  # Uses Hugging Face API now

# @cl.on_message
# async def main(message: cl.Message):
#     if len(messages) > 10:  # ✅ Reset conversation if it gets too long
#         messages[:] = [{'role': 'system', 'content': message.content}]

#     messages.append({'role': 'user', 'content': message.content})  # ✅ Add user input
#     response = ask_order(messages)  # ✅ Generate AI response
#     messages.append({'role': 'assistant', 'content': response})  # ✅ Store AI response

#     await cl.Message(content=response).send()  # ✅ Send response back

