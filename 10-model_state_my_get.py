#!/usr/bin/python3
'''
script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, orm
import sqlalchemy

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    search = argv[4]
    Base.metadata.create_all(engine)

    session = orm.sessionmaker(bind=engine)()

    states = session.query(State).order_by(
             State.id).filter(State.name == search).all()

    if(states):
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
