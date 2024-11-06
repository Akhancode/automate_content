from database import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to Engagement table
    engagements = db.relationship('Engagement', backref='article', lazy=True)


class Engagement(db.Model):
    __tablename__ = 'engagements'

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    views = db.Column(db.Integer, default=0)
    shares = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
