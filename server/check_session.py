# resources/check_session.py
from flask import session, jsonify
from flask_restful import Resource

class CheckSession(Resource):
    def get(self):
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            if user:
                return jsonify({'id': user.id, 'username': user.username, 'image_url': user.image_url, 'bio': user.bio}), 200
        return jsonify({'error': 'Unauthorized'}), 401