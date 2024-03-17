import os
import streamlit as st
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_response(prompt):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": f"{prompt}",
    })

    try:
        generated_text = output[0]['generated_text']
    except KeyError:
        print('KeyError encountered when accessing "generated_text"')
        generated_text = 'KeyError encountered when accessing "generated_text"'
    
    return generated_text.replace(prompt, "").strip()


def main():
    #Streamlit
    st.set_page_config(page_title="AI ChatBot", page_icon='🤖')
    st.header('AI ChatBot')
    messages = st.container(height=400)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        response = generate_response(prompt)
        messages.chat_message("assistant").write(f"AiChat: {response}")


if __name__ == '__main__':
    main()