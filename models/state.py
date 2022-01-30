#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
import models
from models.city import City


class State(BaseModel, Base):
    """  Implementation for the State """
    if models.type_storage == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        class State(BaseModel):
            """ define class"""
            name = ''

            @property
            def cities(self):
                cities_list = []
                cities = models.storage.all(city).values()
                for city in cities:
                    if city.state_id == self.id:
                        cities_list.append(city)
                return cities_list
