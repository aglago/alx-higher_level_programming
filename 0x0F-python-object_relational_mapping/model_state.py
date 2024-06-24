#!/usr/bin/python3

"""
A representation of python
connecting to the database
and performing data driven
queries
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class State(Base):
    """Representing a table in database"""
    __tablename__ = "states"

    id = Column(Integer,
                Sequence('id_seq'),
                primary_key=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
