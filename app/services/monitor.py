import time
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
        self.image_generator = ImageGenerator()

    def _initialize_existing_articles(self):
        """Loads initial articles into memory to track new ones."""
        articles = load_articles()
        for article in articles:
            self.existing_ids.add(article['id'])

    def detect_new_articles(self,interval=10):
        """Checks for and processes new articles."""
        while True:
            try:
                print("Scanning new article....")
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
    #         # Create new article record
    #         # article = Article(
    #         #     title=article_data['title'],
    #         #     content=article_data['content'],
    #         #     source_url=article_data.get('url', 'https://example.com')
    #         # )
    #         # article = {}
              print(article_data)
              articleSummary = self.content_processor.summarize(
                    article_data['content']
                )

              articleImage_url = self.image_generator.generate_image_from_text("prompt")

              # Simulating the "post" with a print statement
              mock_social_post(article_data["title"],articleSummary,articleImage_url,)

              # response = save_engagement(data["title"], data["summary"], data["image_url"], data["views"],
              #                                             data["shares"])
              response = save_engagement("title","summary", "image_url", "views","shares")
              return jsonify(response)
    #

    #
    #
    #         # # Save to database
    #         # db.session.add(article)
    #         # db.session.commit()
    #
    #         # Post to social media
    #         # self.social_poster.post_article(article)
    #         #
    #         # article.processed = True
    #         # db.session.commit()
    #
        except Exception as e:
            print(f"Error processing article: {e}")
    #         # db.session.rollback()