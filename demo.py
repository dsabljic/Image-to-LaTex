import base64
import requests
import os

# OpenAI API Key
api_key = os.environ.get("OPENAI_API_KEY", "api key if the env variable is not present")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "./formula.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Imagine you are a LaTeX expert with the ability to accurately transcribe \
            images of handwritten mathematical formulas into LaTeX code. Your task is to analyze \
            an image of a handwritten math formula and provide the corresponding LaTeX code. \
            Please provide only the LaTeX code in your response."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

# {'id': 'chatcmpl-90A44ed34nnhEL1YMQIFezZGDbgB6', 'object': 'chat.completion', 
#  'created': 1709825716, 'model': 'gpt-4-1106-vision-preview', 
#  'usage': {'prompt_tokens': 486, 'completion_tokens': 27, 'total_tokens': 513}, 
#  'choices': [{'message': {'role': 'assistant', 
#  'content': '```latex\n\\sum_{i=1}^{N} i = \\frac{N^2 + N}{2}\n```'}, 'finish_reason': 'stop', 'index': 0}]}
