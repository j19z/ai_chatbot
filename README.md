# AI Chatbot

## Overview
This project is a simple chatbot utilizing the Hugging Face LLM API and Streamlit. It is designed to demonstrate the capabilities of conversational AI using the Mistral model.

## Model
The chatbot is powered by the [Mistral-7B-Instruct-v0.2](https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2) model from Hugging Face. This model is designed to understand and respond to natural language inputs.

## Features
- Simple and intuitive UI with Streamlit.
- Direct API requests to Hugging Face's free server for generating responses.

## Live Demo
You can test the app on Streamlit Cloud: [AI Chatbot Simple](https://ai-chatbot-simple.streamlit.app/)

## Getting Started
To run this project locally, follow these steps:

### Prerequisites
- Python 3.x
- pip

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai_chatbot.git
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Set up your .env file with your Hugging Face API token:
```bash
HUGGINGFACE_API_TOKEN=your_token_here
```
### Usage
Run the Streamlit application:
```bash
streamlit run app.py
```
### Limitations
The chatbot's responses are very limited since it uses the Hugging Face API directly. All API requests are made to Hugging Face's free server, which may have usage limits.

### Contributing
Contributions are welcome! If you have suggestions for improving this chatbot, please feel free to fork the repository, make changes, and submit a pull request.