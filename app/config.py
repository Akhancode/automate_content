import os

class Config:
    # Path to the JSON feed file
    JSON_FEED_PATH = os.path.join(os.path.dirname(__file__), '../data/articles.json')
    # Path to the SQLite database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///content_automation.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONITOR_INTERVAL = 5  # Check for new articles every 10 seconds
