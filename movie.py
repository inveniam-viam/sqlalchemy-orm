from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

# creating a many-to-many relatioship between the Movie and Actor classes
# since many movies can have many actors and vice-versa

movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)


class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)

    title = Column(String)

    release_date = Column(Date)

    actors = relationship("Actor", secondary = movies_actors_association)

    def __init__(self, title, release_date):

        self.title = title
        self.release_date = release_date
