import requests
import os
from typing import Optional
import logging
from app.config import Config


class ImageGenerator:
    def __init__(self):
        """Initialize the image generator with API configuration."""
        self.api_key = Config.IMAGE_API_KEY
        self.api_url = "https://api.openai.com/v1/images/generations"
        self.default_image = "https://placeholder.com/400x300"

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def generate_image(self,
                       title: str,
                       summary: str,
                       size: str = "1024x1024") -> str:
        """
        Generate an image based on article title and summary using DALL-E API.

        Args:
            title (str): Article title
            summary (str): Article summary
            size (str): Desired image size

        Returns:
            str: URL of the generated image or default placeholder
        """
        if not self.api_key:
            self.logger.warning("No API key provided. Using default image.")
            return self.default_image

        try:
            # Create prompt from title and summary
            prompt = self._create_image_prompt(title, summary)

            # Call DALL-E API
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }

            payload = {
                "prompt": prompt,
                "n": 1,
                "size": size
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                image_url = response.json()['data'][0]['url']
                return image_url
            else:
                self.logger.error(f"API Error: {response.text}")
                return self.default_image

        except Exception as e:
            self.logger.error(f"Error generating image: {str(e)}")
            return self.default_image

    def _create_image_prompt(self,
                             title: str,
                             summary: str,
                             max_length: int = 1000) -> str:
        """
        Create an optimized prompt for image generation.

        Args:
            title (str): Article title
            summary (str): Article summary
            max_length (int): Maximum prompt length

        Returns:
            str: Optimized prompt for image generation
        """
        # Extract key elements from title and summary
        prompt_elements = [
            title.strip(),
            summary[:100].strip()  # Use first 100 chars of summary
        ]

        # Combine elements into a descriptive prompt
        base_prompt = (f"Create a professional illustration for an article titled "
                       f"'{prompt_elements[0]}'. The image should capture the "
                       f"essence of: {prompt_elements[1]}")

        # Add style guidelines
        style_guidelines = (". Style: modern, professional, suitable for "
                            "social media, high quality, detailed illustration")

        # Combine and truncate if needed
        prompt = base_prompt + style_guidelines
        if len(prompt) > max_length:
            prompt = prompt[:max_length - 3] + "..."

        return prompt

    def _validate_image(self, image_url: str) -> bool:
        """
        Validate if the generated image URL is accessible.

        Args:
            image_url (str): URL to validate

        Returns:
            bool: True if valid, False otherwise
        """
        try:
            response = requests.head(image_url)
            return response.status_code == 200
        except:
            return False