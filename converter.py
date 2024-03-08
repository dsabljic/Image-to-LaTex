import base64
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    print("API key not found. Please check your .env file.")
else:
    print(f"API key loaded successfully. {api_key}")

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

response = response.json()

def get_latex():
  try:
    latex_code = response['choices'][0]['message']['content']

    # Strip the markdown code
    if latex_code.startswith('```latex') and latex_code.endswith('```'):
        latex_code = latex_code.replace('```latex', '').replace('```', '').strip()

    print(latex_code)

  except (KeyError, IndexError, TypeError):
    print("The response did not contain LaTeX code in the expected format.")