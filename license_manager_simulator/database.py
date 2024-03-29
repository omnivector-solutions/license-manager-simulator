from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from license_manager_simulator.config import settings

engine = create_engine(settings.DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()
