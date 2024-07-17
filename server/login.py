# resources/login.py
from flask import request, session, jsonify
from flask_restful import Resource
from models import User

class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 422
        user = User.query.filter_by(username=data['username']).first()
        if user and user.password == data['password']:
            session['user_id'] = user.id
            return jsonify({'id': user.id, 'username': user.username, 'image_url': user.image_url, 'bio': user.bio}), 200
        return jsonify({'error': 'Unauthorized'}), 401

