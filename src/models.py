from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date, func
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, default=func.current_date(), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    
    favorites = relationship("Favorite", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "email": self.email,
            "name": self.name,
            "first_name": self.first_name,
            "last_name": self.last_name
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(Enum("arid", "temperate", "tropical", "frozen", "murky", name="climate_types"), nullable=False)
    name = db.Column(db.String(250), nullable=False)

class Character(db.Model):
    __tablename__ = 'character'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))

class Favorite(db.Model):
    __tablename__ = 'favorite'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    character_id = db.Column(db.Integer, ForeignKey('character.id'), nullable=True)
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'), nullable=True)
    
    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")
