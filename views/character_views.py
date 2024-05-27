from flask import jsonify
from flask_restful import Resource, request, reqparse
from models.character import Character
from sqlalchemy import inspect


def validate_response(data, model_id):
    """
    Validates the response data against the model's columns.

    Args:
        data (dict): The data to validate.
        model_id (Model): The SQLAlchemy model instance.

    Returns:
        tuple: The validated data and HTTP status code.
    """

    inspector = inspect(model_id.__class__)
    for key, value in data.items():
        column = inspector.columns.get(key)
        if column is None:
            return {
                'message': f'El campo "{key}", no existe'
            }, 400
        
        if not isinstance(value, column.type.python_type):
            return {
                'message': f'El campo "{key}", es incorrecto.'
            }, 400

    return data, 200


class CharacterAdd(Resource):
    """
    Resource for adding a new Character.
    """

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', 
            type=str, 
            required=True, 
            nullable=False, 
            help="Name no puede estar vacio y debe ser texto")
        parser.add_argument('character_id', 
            type=int, 
            required=True, 
            nullable=False, 
            help="Character ID no puede estar vacio y debe ser int")
        parser.add_argument('height', 
            type=float, 
            required=True, 
            nullable=False, 
            help="Height no puede estar vacio y debe ser decimal")
        parser.add_argument('mass', 
            type=float, 
            required=True, 
            nullable=False,
            help="Mass no puede estar vacio y debe ser decimal")
        parser.add_argument('hair_color', 
            type=str, 
            required=True, 
            nullable=False,
            help="Hair color no puede estar vacio y debe ser texto")
        parser.add_argument('skin_color', 
            type=str, 
            required=True, 
            nullable=False,
            help="Skin color no puede estar vacio y debe ser texto")
        parser.add_argument('eye_color', 
            type=str, 
            required=True, 
            nullable=False,
            help="Eye color no puede estar vacio y debe ser texto")
        parser.add_argument('birth_year', 
            type=int, 
            required=True, 
            help="Birth year no puede estar vacio y debe ser texto")
        args = parser.parse_args()

        if Character.query.filter_by(character_id=args['character_id']).first():
            return {
                'message': f'El Personaje con ese ID ({args["character_id"]}), ya existe.'
            }, 400
        
        character_id = Character(**args)
        character_id.save()
        return validate_response(args, character_id)


class CharacterGet(Resource):
    """
    Resource for getting a Character by its ID.
    """

    def get(self, character_id):
        character_id = Character.query.filter_by(character_id=character_id).first()
        if character_id is None:
            return {
                'message': f'Personaje no encontrado'
            }, 400
        character_data = character_id.__dict__
        character_data.pop('_sa_instance_state')
        return validate_response(character_data, character_id)


class CharacterGetAll(Resource):
    """
    Resource for getting all Characters.
    """

    def get(self):
        character_ids = Character.query.all()
        if character_ids is None:
            return {
                'message': f'No hay personajes registrados'
            }, 400
        character_datas = []
        for character_id in character_ids:
            character_data = character_id.__dict__
            character_data.pop('_sa_instance_state')
            character_datas.append(character_data)
            validation_response, is_valid, = validate_response(character_data, character_id)
            if is_valid == 400:
                return validation_response

        return character_datas

class CharacterDelete(Resource):
    """
    Resource for deleting a Character by its ID.
    """

    def delete(self, character_id):
        character_id = Character.query.filter_by(character_id=character_id).first()
        if character_id is None:
            return {
                'message': f'Personaje no encontrado'
            }, 400
        character_id.delete()
        return {
            'message': f'Personaje, eliminado'
        }, 200
