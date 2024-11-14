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

def truncate_tweet_text(summary, article_url, max_length=280):
    # Reserve characters for URL and newlines
    url_length = len(article_url)
    spacing = len("\n\n")  # for the two newlines
    
    # Calculate remaining characters for summary
    available_chars = max_length - (url_length + spacing)
    
    if available_chars <= 0:
        # If URL itself is too long (shouldn't happen with normal URLs)
        return article_url
    
    # Truncate summary if needed and add ellipsis
    if len(summary) > available_chars:
        summary = summary[:available_chars-3] + "..."
    
    return f"{summary}\n\n{article_url}"

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