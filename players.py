from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to Postgres database
engine = create_engine('postgresql://postgres@localhost:5432/skyl')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Players(Base):
    __tablename__ = "players"

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    school = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    phone_name = Column(String, nullable=False)
