from app.config import Config
import requests



class ImageGenerator:
    def __init__(self):
        """Initialize the image generator with API configuration."""
        self.api_key = Config.IMAGE_API_KEY
        self.api_url = "https://api.openai.com/v1/images/generations"
        self.default_image = "https://placeholder.com/400x300"

    def generate_image_from_text(self,prompt):
        return self.default_image

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