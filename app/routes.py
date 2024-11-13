import os

from flask import Blueprint, jsonify , request
from .services import  save_engagment,image_generator
from .models import Engagement
from .services.social_poster import post_image_with_summary_on_linkedin

# Blueprint for organizing routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/status', methods=['GET'])
def status():
    # accessToken = os.getenv('LINKEDIN_API')
    # sub = os.getenv('LINKEDIN_APP_ID')
    # owner_id = f"urn:li:person:{sub}"
    # image_path = 'D:/Personal/Interview Assessment/LCX/BE/images/cat.jpeg'
    # summary = "Test summary"
    # result = post_image_with_summary_on_linkedin(accessToken,image_path,summary,owner_id)
  
    return jsonify({"status": "Service is up and running"})
@main_bp.route('/image-generate', methods=['GET'])
def image_generate():
    data = request.get_json()
    img=image_generator.ImageGenerator("https://placeholder.com/400x300")
    # using - stable diffusion api
    imageurl =img.generate_image_from_text(data["prompt"])

    # imageurl =img.generate_image_replicate(data["prompt"])
    # imageurl =img.generate_image_from_text_deep_ai(data["prompt"])
    # imageurl =img.generate_dalle_image(data["prompt"])

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