from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://usr:@localhost:5432/sqlalchemy')           # creating a SQLAlchemy engine to interact with postgres DB (obscuring credentials on purpose)

Session = sessionmaker(bind = engine)                                               # creates a SQLAlchemy ORM Session factory bound to this engine

Base = declarative_base()                                                           # creates a base class for our class definitions
