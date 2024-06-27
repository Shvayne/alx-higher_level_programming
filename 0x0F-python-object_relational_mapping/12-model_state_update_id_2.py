#!/usr/bin/python3
"""This script changes the name of a state obj from the db"""
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
        state = session.query(State).filter_by(id=2).first()
        if state:
            state.name = 'New Mexico'
            session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
