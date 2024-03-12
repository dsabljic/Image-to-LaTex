import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

def get_latex_from_image(base64_image):
    """
    Takes a base64 encoded image and makes an OpenAI API call to get the LaTeX code.

    Parameters:
    base64_image (str): Base64 encoded string of the image.

    Returns:
    str: The extracted LaTeX code from the response.
    """

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
                        "text": "Imagine you are a LaTeX expert with the ability to accurately transcribe images of handwritten mathematical formulas into LaTeX code. Your task is to analyze an image of a handwritten math formula and provide the corresponding LaTeX code. Please provide only the LaTeX code in your response. If the user hasn't provided any input just return 'Please provide a handwritten formula or upload an image of the formula.'"
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
    response_data = response.json()

    try:
        latex_code = response_data['choices'][0]['message']['content']
        if latex_code.startswith('```latex') and latex_code.endswith('```'):
            latex_code = latex_code.replace('```latex', '').replace('```', '').strip()
        return latex_code
    except (KeyError, IndexError, TypeError):
        print("The response did not contain LaTeX code in the expected format.")
        return None

# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

## Demo
# if __name__ == "__main__":
#     image_path = "./formula.png"
#     base64_image = encode_image(image_path)
#     latex_code = get_latex_from_image(base64_image)
#     print(latex_code)