from flask import jsonify
from flask_restful import Resource
import db


class DbInit(Resource):
    """
    Resource to initialize the database.
    """

    def get(self):
        try:
            db.init_db()
            data = {
                'success': True, 
                'message': 'Base de datos Iniciada'
            }
            return data, 200
        except:
            data = {
                'success': False,
                'message': 'Error al iniciar la base de datos'
            }
            return data, 400

class DbEnd(Resource):
    """
    Resource to drop the database tables.
    """

    def get(self):
        try:
            db.drop_db()
            data = {
                'success': True,
                'message': 'Tablas eliminadas de la base de datos'
            }
            return data, 200
        except:
            data = {
                'success': False,
                'message': 'Error al eliminar las tablas de la base de datos'
            } 
            return data, 400