# services/social_poster.py
import os
import time
import io
import requests
import json


def post_image_with_summary_on_linkedin(access_token, image_path, summary, linkedin_urn):
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

    # Create upload session
    response = requests.post(upload_url_endpoint, headers=headers, json=payload)
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
                    "text": summary  # This is the text summary of the post
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
        print("Post created successfully!")
    else:
        print(f"Error creating post: {post_response.status_code}, {post_response.text}")


# Example usage
# access_token = 'your_access_token'  # Replace with your access token
# image_path = 'path_to_your_image.jpg'  # Replace with the path to your image
# summary = 'Here is a summary of the post with an image!'
# linkedin_urn = "urn:li:person:your_linkedin_person_urn"  # Replace with your LinkedIn person or organization URN



def mock_social_post(title, summary, image_url, article_url="https://example.com/full-article"):
    post = {
        "title": title,
        "summary": summary,
        "image_url": image_url,
        "article_url": article_url,
    }
    print("💥Mock Social Media Post:", post)


    return post
