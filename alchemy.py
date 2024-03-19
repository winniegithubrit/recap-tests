from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    description = Column(String)

if __name__ == '__main__':
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///student_records.db'

    # Initialize SQLAlchemy engine and session
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create all tables
    Base.metadata.create_all(engine)
