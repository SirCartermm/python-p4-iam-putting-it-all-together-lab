# resources/logout.py
from flask import session, jsonify
from flask_restful import Resource

class Logout(Resource):
    def delete(self):
        if 'user_id' in session:
            session.pop('user_id')
            return jsonify({}), 204
        return jsonify({'error': 'Unauthorized'}), 401