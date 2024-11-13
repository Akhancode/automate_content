# services/social_poster.py
import requests
import os
import tweepy
import time
import io
import json

defaultImagePath = os.path.join("images", "cat.jpeg")

def post_image_with_summary_on_linkedin(access_token, image_path, summary, linkedin_urn,articleUrl):
    try:
        # Step 1: Create an upload session
        upload_url_endpoint = "https://api.linkedin.com/v2/assets?action=registerUpload"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json"
        }

        # Request body for upload session
        payload = {
            "registerUploadRequest": {
                "owner": linkedin_urn,  # LinkedIn Person or Organization URN
                "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
                "serviceRelationships": [{
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }]
            }
        }
        print(json.dumps(payload))

        # Create upload session
        response = requests.post(upload_url_endpoint, headers=headers, json=payload)
        print(response)
        print("access_token, image_path, summary, linkedin_urn,articleUrl")
        
        if response.status_code != 200:
            print(f"Error creating upload session: {response.status_code}, {response.text}")
            return
        upload_url = response.json()["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
        asset_urn = response.json()["value"]["asset"]

        # Step 2: Upload the image file
        with open(image_path, 'rb') as image_file:
            upload_response = requests.post(upload_url, files={'file': image_file})
            if upload_response.status_code != 201:
                print(f"Error uploading image: {upload_response.status_code}, {upload_response.text}")
                return
            print("Image uploaded successfully.")

        # Step 3: Create a post with the image and summary
        post_url = "https://api.linkedin.com/v2/ugcPosts"
        post_payload = {
            "author": linkedin_urn,  # Use the LinkedIn Person or Organization URN here
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": f"{summary}\n\n{articleUrl}"  # This is the text summary of the post
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [{
                        "status": "READY",
                        "description": {
                            "text": "This is an image summary."
                        },
                        "media": asset_urn,  # Use the asset URN of the uploaded image
                        "title": {
                            "text": "Your Image Title"
                        }
                    }]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        # Make the POST request to LinkedIn API
        post_response = requests.post(post_url, headers=headers, json=post_payload)

        if post_response.status_code == 201:
            print("LinkedIn Post created successfully!")
        else:
            print(f"Error creating post: {post_response.status_code}, {post_response.text}")
    except Exception as e:
        print(f"Error linked in  article: {e}")

def post_tweet_with_image(summary,articleUrl, image_path):
    # Your Twitter API credentials from environment variables
    API_KEY = os.getenv('X_CONSUMER_API_KEY')
    API_SECRET_KEY = os.getenv('X_CONSUMER_API_SECRET')
    ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN_KEY')
    ACCESS_TOKEN_SECRET = os.getenv('X_ACCESS_TOKEN_SECRET')
    X_BEARER_TOKEN = os.getenv('X_BEARER_TOKEN')

    # Initialize the Tweepy client with API credentials
    client = tweepy.Client(
        bearer_token=X_BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET_KEY,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    # Authenticate using OAuth1 for media upload
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Upload media and post tweet
    media = api.media_upload(image_path)
    response = client.create_tweet(text=f"{summary}\n\n{articleUrl}", media_ids=[media.media_id])

    print("Tweet posted successfully!", response)
    return response


def mock_social_post(title, summary, image_url=defaultImagePath, article_url="https://example.com/full-article"):
    post = {
        "title": title,
        "summary": summary,
        "image_url": image_url,
        "article_url": article_url,
    }

    accessToken = os.getenv('LINKEDIN_API')
    sub = os.getenv('LINKEDIN_APP_ID')
    owner_id = f"urn:li:person:{sub}"
    print("hdfkdf")
    post_image_with_summary_on_linkedin(accessToken, image_url, summary, owner_id,article_url)
    post_tweet_with_image(summary,article_url,image_url)
    # print("💥Mock Social Media Post:", post)


    return post
