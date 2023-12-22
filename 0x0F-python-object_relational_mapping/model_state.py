#!/usr/bin/python3
"""Start link class to table in database 
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Create state class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def repr(self):
        return f"{self.id}: {self.name}"
