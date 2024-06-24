#!/usr/bin/python3
"""A script using SQLAlchemy to chech if rows in a db contain the letter 'a'."""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    )
    engine = create_engine(engine_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    a_states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in a_states:
        print("{}: {}".format(state.id, state.name))

    session.close()
