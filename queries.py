from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date

# 2 - extract a session
session = Session()

# 3 - extract all movies
movies = session.query(Movie).all()

# 4 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

# 5 - get movies after 15-01-01
movies = session.query(Movie) \
    .filter(Movie.release_date > date(2015, 1, 1)) \
    .all()

print('### Recent movies:')
for movie in movies:
    print(f'{movie.title} was released after 2015')
print('')

# 6 - movies that Sir Kenneth Branagh participated
kenny_movies = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == 'Sir Kenneth Branagh') \
    .all()

print('### Kenneth Branagh movies:')
for movie in kenny_movies:
    print(f'Gilderoy Lockhart starred in {movie.title}')
print('')

# 7 - get actors that have house in Vancouver
vancouver_boys = session.query(Actor) \
    .join(ContactDetails) \
    .filter(ContactDetails.address.ilike('%vancouver%')) \
    .all()

print('### Actors that live in Vancouver:')
for actor in vancouver_boys:
    print(f'{actor.name} has a house in Vancouver')
print('')
