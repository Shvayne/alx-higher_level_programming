#!/usr/bin/python3
"""This script lists all state objects from the db"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    eng_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(eng_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")

