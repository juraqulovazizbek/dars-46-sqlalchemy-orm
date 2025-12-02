from datetime import datetime
from sqlalchemy import (
    Column, String, Boolean, Float, Integer, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from .db import Base


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    birthdate = Column(DateTime, nullable=False)
    gender = Column(String(20), nullable=False)
    bio = Column(String(256))
    gpa = Column(Float, nullable=False)

    certificates = relationship(
        'Certificate',
        back_populates='student',
        cascade="all, delete"
    )

    def __str__(self):
        return f"Student(id={self.student_id}, name={self.first_name} {self.last_name})"

    def __repr__(self):
        return self.__str__()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Certificate(Base):
    __tablename__ = 'certificates'

    id = Column(Integer, primary_key=True, nullable=False)
    student_id = Column(Integer, ForeignKey("students.student_id", ondelete="CASCADE"))

    title = Column(String(256), nullable=False)
    content = Column(Text, nullable=False)
    issued_at = Column(DateTime, default=datetime.now)
    certificate_code = Column(String(256), unique=True)
    is_verified = Column(Boolean, default=False)

    student = relationship('Student', back_populates='certificates')

    def __str__(self):
        return f"Certificate(title={self.title}, student_id={self.student_id})"

    def __repr__(self):
        return f"<Certificate id={self.id}, title='{self.title}', student_id={self.student_id}>"
