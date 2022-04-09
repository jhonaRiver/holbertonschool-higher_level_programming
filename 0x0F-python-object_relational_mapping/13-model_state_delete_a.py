#!/usr/bin/python3
'''
script that deletes all State objects with a name containing the letter a from
the database hbtn_0e_6_usa
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, orm
import sqlalchemy

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = orm.sessionmaker(bind=engine)()

    states = session.query(State).all()

    for state in states:
        if ('a' in state.name):
            session.delete(state)

    session.commit()

    session.close()
