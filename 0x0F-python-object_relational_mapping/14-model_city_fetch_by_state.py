#!/usr/bin/python3
"""
listing all cities of a state
"""

from sqlalchemy import (create_engine)
import sys
from sqlalchemy.orm import Session
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(user, passwd, db_name))

    session = Session(bind=engine)

    instances = session.query(State.name, City.id, City.name)\
        .order_by(City.id).filter(State.id == City.state_id)
    for instance in instances:
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
