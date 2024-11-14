import os
import tweepy
import requests
from flask import Blueprint, jsonify , request ,render_template
from .services import  save_engagment,image_generator
from .models import Engagement
from .services.social_poster import post_image_with_summary_on_linkedin,post_tweet_with_image
from .utils import load_articles,append_article
# Blueprint for organizing routes
main_bp = Blueprint('main', __name__)


sample_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "interests": ["programming", "reading", "hiking"]
}

@main_bp.route('/')
def display_json():
    return render_template('display.html')

@main_bp.route('/get-articles', methods=['GET'])
def get_articles():
    # Load articles from your data source (e.g., database, file)
    articles = load_articles()  # Assume this function fetches the articles
    return jsonify(articles)


@main_bp.route('/add-article', methods=['POST'])
def add_article():
    data = request.get_json()  # Get the JSON data from the frontend
    title = data.get('title')
    content = data.get('content')
    article_url = data.get('articleUrl')
    views = data.get('views')

    # Save the article data to a database or perform other operations
    append_article(data)

    # Return a success response
    response = {
        'status': 'success',
        'message': 'Article added successfully',
    }
    return jsonify(response)

@main_bp.route('/test', methods=['GET'])
def test():
    try:
        print("test")
        # Attempt the GET request to LinkedIn API
        response = requests.get(url="https://api.linkedin.com/v2/userinfo")

        # Check if the request was successful (HTTP 200)
        response.raise_for_status()  # This will raise an HTTPError for 4xx/5xx responses
        user_info = response.json()
        
        return jsonify({
            "status": "Service is up and running",
            "user_info": user_info  # Include user info if you want to see it in response
        })

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (like 404, 403, 500)
        return jsonify({
            "error": "HTTP error occurred",
            "details": str(http_err),
            "status_code": response.status_code
        }), response.status_code

    except requests.exceptions.ConnectionError:
        # Handle network errors (e.g., server unreachable)
        return jsonify({
            "error": "Connection error occurred. LinkedIn API might be down."
        }), 503

    except requests.exceptions.Timeout:
        # Handle timeout errors
        return jsonify({
            "error": "Request timed out. LinkedIn API took too long to respond."
        }), 504

    except requests.exceptions.RequestException as req_err:
        # Handle any other request-related errors
        return jsonify({
            "error": "An error occurred while trying to connect to LinkedIn API.",
            "details": str(req_err)
        }), 500


@main_bp.route('/status', methods=['GET'])
def status():
    # Your Twitter API credentials
    # post_tweet_with_image("testing Summary xyz","http://localhost:9000",os.path.join("images", "cat.jpeg"))
  
    return jsonify({"status": "Service is up and running"})
@main_bp.route('/image-generate', methods=['GET'])
def image_generate():
    data = request.get_json()
    img=image_generator.ImageGenerator("https://placeholder.com/400x300")
    # using - stable diffusion api
    imageurl =img.generate_image_from_text(data["prompt"])

    print(imageurl)
    return jsonify({"imageUrl": imageurl})
@main_bp.route('/engagement', methods=['POST'])
def engagement():
    data = request.get_json()
    response= save_engagment.save_engagement(data["title"],data["summary"],data["image_url"],data["views"],data["shares"])
    return jsonify(response)

@main_bp.route('/engagement', methods=['GET'])
def getAllEngagement():
    allEngagements= Engagement.query.all()
    response = [engagement.to_dict() for engagement in allEngagements]
    return jsonify(response)


@main_bp.route('/top-engagements', methods=['GET'])
def get_top_engagements():
    query_type = request.args.get('type',"default")
    if query_type == 'most_shared':
        
        top_engagements = Engagement.query.order_by(Engagement.shares.desc()).limit(3).all()
    elif query_type == 'most_viewed':
        top_engagements = Engagement.query.order_by(Engagement.views.desc()).limit(3).all()
    else :
        # Both - default case
        top_engagements_views = Engagement.query.order_by(Engagement.views.desc()).limit(3).all()
        top_engagements_shares = Engagement.query.order_by(Engagement.shares.desc()).limit(3).all()
        view_results = [engagement.to_dict() for engagement in top_engagements_views]
        shares_results = [engagement.to_dict() for engagement in top_engagements_shares]
        return jsonify({
            "top_3_by_views": view_results,
            "top_3_by_shares": shares_results
        }), 200


    results = [engagement.to_dict() for engagement in top_engagements]
    print(query_type,"----------------------------")
    return jsonify(results), 200