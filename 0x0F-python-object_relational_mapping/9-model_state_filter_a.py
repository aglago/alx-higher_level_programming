#!/usr/bin/python3

"""using sqlalchemy to query data
from database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # establishing connection with the database
    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(username, password, db_name))

    # database tracker
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).\
            order_by(State.id).filter(State.name.like('%a%')):
        print("{}: {}".format(instance.id, instance.name))
