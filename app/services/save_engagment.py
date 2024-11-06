from ..models import db , Engagement
def save_engagement(title, summary, image_url,views=0,shares=0):
    """
    Save the engagement data to the SQLite database.
    """
    article_url = "https://example.com/full-article"
    engagement = Engagement(
        title=title,
        summary=summary,
        image_url=image_url,
        article_url=article_url,
        views=views,
        shares=shares
    )
    db.session.add(engagement)
    db.session.commit()
    return engagement.to_dict()