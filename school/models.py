from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Date, DateTime, Text,
)
from .db import Base


class Student(Base):
    __tablename__ = 'students'

    student_id = Column('id', Integer, primary_key=True, nullable=False)
    first_name = Column('first_name', String(length=64), nullable=False)
    last_name = Column('last_name', String(length=64), nullable=False)
    birthdate = Column('birth_date', Date, nullable=False)
    bio = Column('bio', Text)

    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)

