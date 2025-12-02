from datetime import datetime
from sqlalchemy import DateTime
from school.create_tables import init_db
import random 
from school.crud import (
    create_student,
    get_students,
    get_one_student_by_id,
    update_student,
    create_certificate,
    get_all_certificates,
    get_unverified_certificates,
    get_certificates_by_student,
    get_certificate_by_code,
    get_last_five_certificates,
)
from school.db import get_db

init_db()


# create_student('ali', 'valiyev3', date(2005, 9, 3), 'male', 'matematik', 4.5)

# students = get_students()
# print(students)


# one_student = get_one_student_by_id(2)
# print(one_student.first_name, one_student.gpa)

# update = update_student(2, gpa= 2.22)



# def generate_certificate_code():
#     return str(random.randint(10000000, 99999999))

# create_certificate(
#     student_id=6,
#     title='Learn Python3',
#     content='Bu sertifikat Python3 ni mukammal urganganlarga beriladi',
#     issued_at=datetime.utcnow(),
#     certificate_code=generate_certificate_code(),
#     is_verified=True
# )


# all_certificates = get_all_certificates()
# for c in all_certificates:
#     print(c.certificate_code, c.title, c.is_verified)


# unverified = get_unverified_certificates()
# for c in unverified:
#     print(c.certificate_code, c.title, c.is_verified)


# student_certificates = get_certificates_by_student(1)
# for c in student_certificates:
#     print(c.title, c.issued_at)



last_five = get_last_five_certificates()
for c in last_five:
    print(c.certificate_code, c.title, c.issued_at, f"Student id: {c.student_id}" )