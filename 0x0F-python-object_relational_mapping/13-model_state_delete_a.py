#!/usr/bin/python3
"""This script deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(States).filter(State.name.like('%a%')).all()
        for s in state:
            session.delete(s)
        session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()

