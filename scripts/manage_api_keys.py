from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env.py
load_dotenv()

# Database connection using SQLAlchemy
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///api_keys.db")
engine = create_engine(DATABASE_URL)

Base = declarative_base()

# Define the APIKey model
class APIKey(Base):
    __tablename__ = "api_keys"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    api_key = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Session for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def add_api_key(username, api_key):
    with SessionLocal() as session:
        db_api_key = APIKey(username=username, api_key=api_key)
        session.add(db_api_key)
        session.commit()

def update_api_key(username, new_api_key):
    with SessionLocal() as session:
        session.execute(
            text("UPDATE api_keys SET api_key = :new_key WHERE username = :username"),
            {"new_key": new_api_key, "username": username},
        )
        session.commit()

def remove_api_key(username):
    with SessionLocal() as session:
        session.execute(text("DELETE FROM api_keys WHERE username = :username"), {"username": username})
        session.commit()

def get_api_key(username):
    with SessionLocal() as session:
        result = session.query(APIKey.api_key).filter(APIKey.username == username).first()
        return result[0] if result else None

# Example usage
add_api_key('bob', 'apikey_bob')
add_api_key('joe', 'apikey_joe')
add_api_key('sally', 'apikey_sally')

# Update API key for Joe
update_api_key('joe', 'new_apikey_joe')

# Remove API key for Sally
remove_api_key('sally')

# Get API key for Bob
bob_api_key = get_api_key('bob')
print(f"Bob's API key: {bob_api_key}")

