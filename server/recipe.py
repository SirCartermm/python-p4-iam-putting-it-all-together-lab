from flask import session, request, jsonify
from flask_restful import Resource
from models import Recipe, User

class Recipe(Resource):
    def get(self, id):
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            if user:
                recipe = Recipe.query.get(id)
                if recipe:
                    return jsonify({'id': recipe.id, 'title': recipe.title, 'instructions': recipe.instructions, 'inutes_to_complete': recipe.minutes_to_complete, 'user': {'id': user.id, 'username': user.username, 'image_url': user.image_url, 'bio': user.bio}}), 200
                return jsonify({'error': 'Recipe not found'}), 404
        return jsonify({'error': 'Unauthorized'}), 401

    def put(self, id):
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            if user:
                recipe = Recipe.query.get(id)
                if recipe:
                    data = request.get_json()
                    if not data:
                        return jsonify({'error': 'Invalid request'}), 422
                    recipe.title = data['title']
                    recipe.instructions = data['instructions']
                    recipe.minutes_to_complete = data['minutes_to_complete']
                    try:
                        db.session.commit()
                        return jsonify({'id': recipe.id, 'title': recipe.title, 'instructions': recipe.instructions, 'inutes_to_complete': recipe.minutes_to_complete, 'user': {'id': user.id, 'username': user.username, 'image_url': user.image_url, 'bio': user.bio}}), 200
                    except:
                        return jsonify({'error': 'Invalid request'}), 422
                return jsonify({'error': 'Recipe not found'}), 404
        return jsonify({'error': 'Unauthorized'}), 401
