import os

class Config:
    # Path to the JSON feed file
    JSON_FEED_PATH = os.path.join(os.path.dirname(__file__), '../data/articles.json')
    # Path to the SQLite database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///content_automation.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONITOR_INTERVAL = 2  # Check for new articles every 10 seconds
    IMAGE_API_KEY = "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"