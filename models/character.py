from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from db import Model, db_session
import logging
log = logging.getLogger(__name__)

class Character(Model):
    """
    Character model to represent character data in the database.

    Attributes:
        id (int): Unique identifier of the character.
        character_id (int): Externally provided unique identifier of the character.
        name (str): Name of the character.
        height (float): Height of the character.
        mass (float): Mass of the character.
        hair_color (str): Hair color of the character.
        skin_color (str): Skin color of the character.
        eye_color (str): Eye color of the character.
        birth_year (int): Birth year of the character.
    """

    __tablename__ = 'characters'

    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    height: Mapped[float] = mapped_column(Float(2), default=0)
    mass: Mapped[float] = mapped_column(Float(2), default=0)
    hair_color: Mapped[str] = mapped_column(String(20), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(20), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(20), nullable=False)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        if self.id:
            return f'<Character {self.id}-{self.name}>'
        else:
            return f'<Character>'

    def save(self, *args):
        """
        Saves the Character object to the database.
        """
        try:
            db_session.add(self)
            db_session.commit()
        except Exception as e:
            logging.error({
                'error': e,
                'message': 'Error al guardar los datos'
            })

    def update(self, *args):
        """
        Updates the Character object in the database.
        """
        try:
            db_session.commit()
        except Exception as e:
            logging.error({
                'error': e,
                'message': 'Error al actualizar los datos'
            })

    def delete(self):
        """
        Deletes the Character object from the database.
        """
        try:
            db_session.delete(self)
            db_session.commit()
        except Exception as e:
            logging.error({
                'error': e,
                'message': 'Error al eliminar el registro'
            })
