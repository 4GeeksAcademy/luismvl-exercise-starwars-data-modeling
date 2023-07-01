import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
#     def to_dict(self):
#         return {}


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    full_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    skin_color = Column(String(250))
    birth_year = Column(Date)
    gender = Column(String(250))
    description = Column(String(250))
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)


class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)

class FavoritesCharacters(Base):
    __tablename__ = 'favorites_characters'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    release_date = Column(Date, nullable=False)

class Climate(Base):
    __tablename__ = 'climates'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Terrain(Base):
    __tablename__ = 'terrains'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class CharactersFilms(Base):
    __tablename__ = 'chatacters_films'
    characters_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)

class PlanetsFilms(Base):
    __tablename__ = 'planets_films'
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)

class PlanetsTerrains(Base):
    __tablename__ = 'planets_terrains'
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    terrain_id = Column(Integer, ForeignKey('terrains.id'), primary_key=True)

class PlanetsClimates(Base):
    __tablename__ = 'planets_climates'
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    climate_id = Column(Integer, ForeignKey('climates.id'), primary_key=True)

    


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
