import time
import os
from flask import jsonify
from app.utils import load_articles
from app.services.content_processor import ContentProcessor
from app.services.image_generator import ImageGenerator
from app.services.social_poster import mock_social_post
from app.services.save_engagment import  save_engagement

class ArticleMonitor:
    def __init__(self):
        self.existing_ids = set()
        self._initialize_existing_articles()
        self.content_processor = ContentProcessor()
        self.image_generator = ImageGenerator("https://placeholder.com/400x300")

    def _initialize_existing_articles(self):
        """Loads initial articles into memory to track new ones."""
        articles = load_articles()
        for article in articles:
            self.existing_ids.add(article['id'])

    def detect_new_articles(self,interval=10):
        """Checks for and processes new articles."""
        while True:
            try:
                # print("Scanning new article....")
                articles = load_articles()
                new_articles = [article for article in articles if article['id'] not in self.existing_ids]

                # Process new articles
                for article in new_articles:
                    print(f"New article detected: {article['title']}")
                    self.process_article(article)
                    self.existing_ids.add(article['id'])

                time.sleep(interval)  # Interval to check for new articles
            except Exception as e:
                print(f"Error monitoring articles: {e}")
                time.sleep(interval)
    def process_article(self, article_data):
    #     """Process a new article."""
        try:
              print(article_data)
              articleSummary = self.content_processor.summarize(
                    article_data['content']
                )

              articleImage_url = "https://files.oaiusercontent.com/file-ZcGVGrCcMOG2e1nDaoc7EpRx?se=2024-11-13T12%3A04%3A42Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D2b8868a4-9dff-4250-88c8-bb99ca08a2f0.webp&sig=HbHCd/wAITn7CfhvYlRt6OIWjQVp%2Bu/KCM0oIabXzUs%3D"
              # Generate Image using Stable ai
              if(os.getenv('DEVELOPMENT') != "true"):
                  articleImage_url = self.image_generator.generate_image_from_text(articleSummary)



              # Generate Image using Deep ai - no credit
              # articleImage_url = self.image_generator.generate_image_from_text_deep_ai(articleSummary)

              # Simulating the "post" with a print statement
              mock_social_post(article_data["title"],articleSummary,articleImage_url,article_url=article_data["url"])
              views = article_data.get("views",0)
              shares = article_data.get("shares",0)


              response = save_engagement(article_data["title"], articleSummary, articleImage_url, views,
                                                          shares)
              print ("Stored to DB",jsonify(response))

    #
        except Exception as e:
            print(f"Error processing article: {e}")
    #         # db.session.rollback()