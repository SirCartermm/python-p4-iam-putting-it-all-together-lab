from flask import Flask, request, jsonify
from flask_restful import Api
from resources.signup import Signup
from resources.check_session import CheckSession
from resources.login import Login
from resources.logout import Logout
from resources.recipe_index import RecipeIndex
from resources.recipe import Recipe

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)

api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check-session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(RecipeIndex, '/recipes')
api.add_resource(Recipe, '/recipes/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)