'''
Created on Jun 26, 2017

@author: alinaved
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Engine = create_engine('sqlite:///../../src/db/bondDB', echo=True)
Session = sessionmaker(bind=Engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.create_all(Engine)        