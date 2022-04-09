#!/usr/bin/python3
'''
script that changes the name of a State object from the database hbtn_0e_6_usa
'''


import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).from_statement(text(
        "SELECT * "
        "FROM states "
        "WHERE id=2"
        ))
    state.name = 'New Mexico'
    session.commit()

    session.close()
