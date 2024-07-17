# resources/recipe_index.py
from flask import session, request, jsonify
from flask_restful import Resource
from models import Recipe, User

class RecipeIndex(Resource):
    def get(self):
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            if user:
                recipes = Recipe.query.filter_by(user_id=user_id).all()
                return jsonify([{'id': recipe.id, 'title': recipe.title, 'instructions': recipe.instructions, 'inutes_to_complete': recipe.minutes_to_complete, 'user': {'id': user.id, 'username': user.username, 'image_url': user.image_url, 'bio': user.bio}} for recipe in recipes]), 200
        return jsonify({'error': 'Unauthorized'}), 401

    def post(self):
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            if user:
                data = request.get_json()
                if not data:
                    return jsonify({'error': 'Invalid request'}), 422
                recipe = Recipe(title=data['title'], instructions=data['instructions'], minutes_to_complete=data['minutes_to_complete'], user_id=user_id)
                try:
                    db.session.add(recipe)
                    db.session.commit()
                    return jsonify({'id': recipe.id, 'title': recipe.title, 'instructions': recipe.instructions, 'inutes_to_complete': recipe.minutes_to_complete, 'user': {'id': user.id, 'username': user.username, 'image_url': user.image_url, 'bio': user.bio}}), 201
                except:
                    return jsonify({'error': 'Invalid request'}), 422
        return jsonify({'error': 'Unauthorized'}), 401