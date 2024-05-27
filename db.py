from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:///project.db', echo=True)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Model = declarative_base()
Model.query = db_session.query_property()

def init_db():
    """
    Initializes the database by creating all tables.
    """
    import models.character as character
    Model.metadata.create_all(bind=engine)

def drop_db():
    """
    Drops all tables in the database.
    """
    Model.metadata.drop_all(bind=engine)


def inspect_db():
    return Model.metadata.tables