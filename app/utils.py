import json
from .config import Config

def load_articles():
    """Loads articles from JSON feed."""
    with open(Config.JSON_FEED_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)