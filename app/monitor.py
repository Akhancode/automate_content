import time
from app.utils import load_articles
from app.services.content_processor import ContentProcessor
from app.services.image_generator import ImageGenerator

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
    #         # # Generate summary
              print("summary :", articleSummary)
              print("imageUrl :",articleImage_url)
    #
    #         # # Generate image
    #         # article.image_url = self.image_generator.generate_image(
    #         #     article.title, article.summary
    #         # )
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