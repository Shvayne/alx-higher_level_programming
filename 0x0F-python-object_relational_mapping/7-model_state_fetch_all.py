#!/usr/bin/python3
"""this script lists all the state objects from the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(engine_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))

    session.close()
