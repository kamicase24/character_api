from flask import Flask, render_template
from flask_restful import Resource, Api
from views import db_views, character_views


app = Flask(__name__)
api = Api(app)

    
api.add_resource(db_views.DbInit, '/db/init')
api.add_resource(db_views.DbEnd, '/db/drop')

api.add_resource(character_views.CharacterAdd, 
                    '/character/add', 
                    '/character/new',
                    '/character')

api.add_resource(character_views.CharacterGet,
                    '/character/get/<int:character_id>',
                    '/character/<int:character_id>')

api.add_resource(character_views.CharacterGetAll,
                    '/character/getAll',
                    '/character')

api.add_resource(character_views.CharacterDelete,
                    '/character/delete/<int:character_id>')


@app.route('/docs')
def docs():
    """
    Serves the API documentation HTML page.
    """
    return render_template('docs.html')