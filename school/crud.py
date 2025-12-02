from datetime import datetime
from sqlalchemy import or_, not_, and_
from .models import Student, Certificate
from .db import get_db


def create_student(first_name: str, last_name: str, birthdate: datetime, gender: str, bio: str | None = None, gpa: float | None=None):
    student = Student(
        first_name=first_name,
        last_name=last_name,
        birthdate=birthdate,
        gender = gender,
        bio=bio,
        gpa = gpa,
    )
    
    with get_db() as session:
        session.add(student)
        session.commit()

def get_students() -> list[Student]:
    with get_db() as session:
        students = session.query(Student).all()

    return students

def get_one_student_by_id(student_id):
    with get_db() as session:
        students = session.query(Student).get(student_id)

    return students

def update_student(
        student_id: int | None = None,
        first_name: str | None = None,
        last_name: str | None = None, 
        birthdate: datetime | None = None, 
        gender: str | None = None, 
        bio: str | None = None, 
        gpa: float | None=None
    ):
    
    student = get_one_student_by_id(student_id)

    if student:
        with get_db() as session:
            student.first_name = first_name if first_name else student.first_name
            student.last_name = last_name if last_name else student.last_name
            student.birthdate = birthdate if birthdate else student.birthdate
            student.gender = gender if gender else student.gender
            student.bio = bio if bio else student.bio
            student.gpa = gpa if gpa else student.gpa

            session.add(student)
            session.commit()




def create_certificate(student_id, title, content, issued_at=None, certificate_code=None, is_verified=False):
    certificate = Certificate(
        student_id=student_id,
        title=title,
        content=content,
        issued_at=issued_at,
        certificate_code=certificate_code,
        is_verified=is_verified
    )
    with get_db() as session:
        session.add(certificate)
        session.commit()
        
def get_all_certificates() -> list[Certificate]:
    with get_db() as session:
        certificates = session.query(Certificate).all()
    return certificates

def get_unverified_certificates() -> list[Certificate]:
    with get_db() as session:
        certificates = session.query(Certificate).filter(Certificate.is_verified == False).all()
    return certificates

def get_certificates_by_student(student_id: int) -> list[Certificate]:
    with get_db() as session:
        certificates = session.query(Certificate).filter(Certificate.student_id == student_id).all()
    return certificates

def get_certificate_by_code(certificate_code: str) -> Certificate | None:
    with get_db() as session:
        certificate = session.query(Certificate).filter(Certificate.certificate_code == certificate_code).first()
    return certificate

def get_last_five_certificates() -> list[Certificate]:
    with get_db() as session:
        certificates = session.query(Certificate).order_by(Certificate.issued_at.desc()).all()
    return certificates[:5]