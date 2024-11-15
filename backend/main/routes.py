from flask import Blueprint, jsonify, request, abort


main_bp = Blueprint('main', __name__)

@main_bp.route('/homepage')
def homepage():
    return jsonify({'message': 'Hello, World!'})

