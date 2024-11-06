
from datetime import datetime
# Initialize the SQLAlchemy instance
from app import db

class Engagement(db.Model):
    __tablename__ = 'engagements'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    article_url = db.Column(db.String(200), nullable=False)
    summary = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    views = db.Column(db.Integer, default=0)
    shares = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary,
            "image_url": self.image_url,
            "article_url": self.article_url,
            "views": self.views,
            "shares": self.shares
        }
