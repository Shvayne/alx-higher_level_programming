#!/usr/bin/python3
"""Prints all the city objects from the db"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    output = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in output:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

