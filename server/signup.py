# resources/signup.py
from flask import request, jsonify
from flask_restful import Resource
from models import User

class Signup(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 422
        user = User(**data)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({'id': user.id, 'username': user.username, 'image_url': user.image_url, 'bio': user.bio}), 201
        except:
            return jsonify({'error': 'Username already exists'}), 422