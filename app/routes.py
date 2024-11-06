from flask import Blueprint, jsonify

# Blueprint for organizing routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Service is up and running"})
