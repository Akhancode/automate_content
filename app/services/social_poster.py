# services/social_poster.py

def mock_social_post(title, summary, image_url, article_url):
    post = {
        "title": title,
        "summary": summary,
        "image_url": image_url,
        "article_url": article_url,
    }
    print("Mock Social Media Post:", post)
    return post
