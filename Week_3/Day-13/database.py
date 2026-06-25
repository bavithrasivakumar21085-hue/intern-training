from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="postgresql://postgres:Bavi%40123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base= declarative_base()