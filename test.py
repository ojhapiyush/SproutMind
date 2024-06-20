from dotenv import load_dotenv
import os
import anthropic
import pandas as pd

## anthropic key
client = anthropic.Anthropic(
    api_key= "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",
)

def conversation():
  conversation_history = []

  while True:
    # Get user input for prompt
    user_prompt = input("You: ")

    # Add user prompt to conversation history
    conversation_history.append({"role": "user", "content": user_prompt})

    # Send request and retrieve response
    response = anthropic.Anthropic().messages.create(
        model="claude-2.1",
        system="act as an assistant to a farmer and avoid any questions that are not related to farming by giving a proper excuse",
        max_tokens=1024,
        temperature=0.5,
        messages=conversation_history
    )
    print(f"Claude: {response.content[0].text}")  # Print Claude's response
    conversation_history.append({"role": "assistant", "content": response.content[0].text})

    # Check if user wants to exit
    if user_prompt.lower() == "quit":
      break

  conversation_history.clear()
    
conversation()