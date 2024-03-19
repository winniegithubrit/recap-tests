# seed.py

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy import Base, Student
import random

fake = Faker()

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///student_records.db'

# Initialize SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Create seed data
def create_students(num_students):
    for _ in range(num_students):
        student = Student(
            name=fake.name(),
            email=fake.email(),
            description=fake.text()
        )
        session.add(student)
    session.commit()

if __name__ == '__main__':
    # Ensure that your tables are created before adding seed data
    Base.metadata.create_all(engine)

    # Generate and add seed data
    create_students(10)  # Adjust the number as needed
