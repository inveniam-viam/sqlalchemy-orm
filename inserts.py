# Persisting Data

from datetime import date 

from actor import Actor 
from base import Session, engine, Base 
from contact_details import ContactDetails
from movie import Movie
from stuntman import Stuntman

# generating DB schema

Base.metadata.create_all(engine)


# create new session

session = Session()

# create some movie objects

the_departed = Movie("The Departed", date(2007, 12, 12))
belfast = Movie("Belfast", date(2021, 1, 21))
barbie = Movie("Barbie", date(2023, 7, 21))

# create some actors 

matt_damon = Actor("Matt Damon", date(1970, 10, 8))
kenneth_branagh = Actor("Sir Kenneth Branagh", date(1954, 12, 7))
ryan_gosling = Actor("Ryan Gosling", date(1981, 6, 5))

# add actors to movies

the_departed.actors = [matt_damon]
belfast.actors = [kenneth_branagh]
barbie.actors = [ryan_gosling]

# add contact details

matt_contact = ContactDetails("415 555 2671", "Burbank, CA", matt_damon)
kenny_contact = ContactDetails("423 555 5623", "London, England", kenneth_branagh)
kenny_contact_2 = ContactDetails("421 444 2323", "Belfast, Northern Ireland", kenneth_branagh)
ryan_contact = ContactDetails("421 333 9428", "Vancouver, Canada", ryan_gosling)

# persists

session.add(the_departed)
session.add(belfast)
session.add(barbie)


session.add(matt_contact)
session.add(kenny_contact)
session.add(kenny_contact_2)
session.add(ryan_contact)



# commit and close

session.commit()
session.close()
