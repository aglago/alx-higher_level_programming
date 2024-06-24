#!/usr/bin/python3

"""
A representation of python
connecting to the database
and performing data driven
queries
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

from model_state import Base


class City(Base):
    """Representing a table in database"""
    __tablename__ = "cities"

    id = Column(Integer,
                Sequence('id_seq'),
                primary_key=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
