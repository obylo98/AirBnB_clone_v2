#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
=======
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
