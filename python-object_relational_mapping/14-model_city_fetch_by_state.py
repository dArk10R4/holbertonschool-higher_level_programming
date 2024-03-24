#!/usr/bin/python3
"""
    that prints all City objects from
    the database hbtn_0e_14_usa
"""


from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Use: <mysql username> <mysql password>'
                 ' <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(City.id)

    query = session.query(City).join(State).order_by(City.id).all()
    for obj in query:
        print("{}: ({}) {}".format(obj.state.name, obj.id, obj.name))

    session.close()