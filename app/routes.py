from flask import Blueprint, jsonify , request
from .services import  save_engagment
from .models import Engagement
# Blueprint for organizing routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Service is up and running"})
@main_bp.route('/engagment', methods=['POST'])
def engagment():
    data = request.get_json()
    response= save_engagment.save_engagement(data["title"],data["summary"],data["image_url"],data["views"],data["shares"])
    return jsonify(response)


@main_bp.route('/top-engagements', methods=['GET'])
def get_top_engagements():
    query_type = request.args.get('type')
    if query_type == 'most_shared':
        top_engagements = Engagement.query.order_by(Engagement.shares.desc()).limit(3).all
    elif query_type == 'most_viewed':
        top_engagements = Engagement.query.order_by(Engagement.views.desc()).limit(3).all
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
    return jsonify(results), 200