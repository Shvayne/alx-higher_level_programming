#!/usr/bin/python3
"""A script that prints the first occurance of the state object in the db"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(engine_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
