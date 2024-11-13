
import torch
import random
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
class ImageGenerator:
    def __init__(self, default_image):
        self.default_image = default_image
        
    def generate_image_from_text_deep_ai(self,prompt):
        try:
            # Define the API endpoint for Text-to-Image
            url = "https://api.deepai.org/api/text2img"

            # Send the POST request with the text prompt
            response = requests.post(
                url,
                data={'text': prompt},
                headers={'api-key': os.getenv('DEEPAI_API_KEY')}
            )

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the image URL from the response
                image_url = response.json()['output_url']
                return image_url
            else:
                # If there was an error, print the error message and return None
                print(f"Error: {response.status_code}, {response.text}")
                raise Exception(str(response.json()))
        except Exception as e:
            print(f"Error generating image: {e}")
            return self.default_image

    def generate_image_from_text(self, prompt="cat with shoe"):
        os.makedirs("images", exist_ok=True)
        try:
            # createing random name
            short_prompt = prompt.replace(" ", "")[:10]
            random_number = random.randint(10000, 99999)
            filename = f"{short_prompt}_{random_number}.jpeg"

            url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
            headers = {
                "authorization": f"Bearer {os.getenv('STABILITY_API_KEY')}",
                "accept": "image/*"
            }
            data = {
                "prompt": prompt,
                # "output_format": "jpeg",
                "width": 1024,
                "height": 1024,
                "steps": 50,
                "cfg_scale": 7.0
            }

            response = requests.post(url, headers=headers, files={"none": ''}, data=data)

            if response.status_code == 200:
                # Save the image
                image_path = os.path.join("images", filename)
                with open(image_path, 'wb') as file:
                    file.write(response.content)

                # Return the URL to access the image
                full_path = os.path.abspath(image_path)
                return full_path
            else:
                raise Exception(str(response.json()))
        except Exception as e:
            print(f"Error generating image: {e}")
            return self.default_image