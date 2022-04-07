#!/usr/bin/python3
'''
file that contains the class definition of a State and an instance
Base = declarative_base()
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    Inherits from Base class
    Links MySQL table 'state'

    Instances:
        id: column of an auto-generated, unique integer
        name: column of a string with 128 characters maximum
    '''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
