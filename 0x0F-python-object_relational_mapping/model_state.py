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


class States(Base):
    """Representing a table in database"""
    __tablename__ = "states"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                Sequence('id_seq'))
    name = Column(String(128),
                  nullable=False)
