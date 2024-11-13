import json
from .config import Config
import uuid

def generate_unique_id(articles):
    """Generates a unique ID that does not already exist in the articles."""

    new_id = str(uuid.uuid4())  
    # Ensure the ID is unique
    while any(article.get('id') == new_id for article in articles):
        new_id = str(uuid.uuid4()) 
    return new_id


def load_articles():
    """Loads articles from JSON feed."""
    with open(Config.JSON_FEED_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def append_article(new_article):
    """Appends a new article to the existing articles in the JSON feed with a unique ID."""
    articles = load_articles()
    
    new_id = generate_unique_id(articles)
    
    new_article['id'] = new_id
    articles.append(new_article)
    
    # Write the updated articles back to the JSON feed
    with open(Config.JSON_FEED_PATH, 'w', encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False, indent=4)