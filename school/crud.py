from datetime import datetime
from sqlalchemy import or_, not_, and_
from .models import Student , Score
from .db import get_db


def create_student(first_name: str, last_name: str, birthdate: datetime, bio: str | None = None):
    student = Student(
        first_name=first_name,
        last_name=last_name,
        birthdate=birthdate,
        bio=bio
    )
    
    with get_db() as session:
        session.add(student)
        session.commit()

def get_students() -> list[Student]:
    with get_db() as session:
        students = session.query(Student).all()
    
    return students

def get_one_student(student_id: int) -> Student | None:
    with get_db() as session:
        student = session.query(Student).get(student_id)
    
    return student

def search_students_by_first_name(first_name: str) -> list[Student]:
    with get_db() as session:
        students = session.query(Student).filter(Student.first_name==first_name).all()
    
    return students

def search_students_by_name(name: str) -> list[Student]:
    with get_db() as session:
        students = session.query(Student).filter(
            or_(Student.first_name.like(f'%{name}%'), Student.last_name.like(f'%{name}%'))
        ).all()
    
    return students

def update_student(
    student_id: int | None = None,
    first_name: str | None = None, 
    last_name: str | None = None, 
    birthdate: datetime | None = None, 
    bio: str | None = None
):
    student = get_one_student(student_id)

    if student:
        with get_db() as session:
            student.first_name = first_name if first_name else student.first_name
            student.last_name = last_name if last_name else student.last_name
            student.birthdate = birthdate if birthdate else student.birthdate
            student.bio = bio if bio else student.bio

            session.add(student)
            session.commit()

def delete_student(student_id: int):
    student = get_one_student(student_id)

    if student:
        with get_db() as session:
            session.delete(student)
            session.commit() # commit bu daqat insert sellect update da ishlatiladi lkn kurishda tekshirishda yo'q faqat nmadir uzgarsa gina 

def filter_students_by_gender(gender:str) -> list[Student]:
    with get_db() as session:
        # result = session.query(Student).filter(Student.gender==gender).all()
        result = session.query(Student).filter_by(gender=gender).all()          #felter_by da birdaniga yozib ketsa bular ekan vaqtdan yutish uchun bir xil ishledi 
    return result

def filter_students_by_gpa(min_gpa: float , max_gpa: float) -> list[Student]:
    with get_db() as session:
        # result = session.query(Student).filter(Student.gpa >= min_gpa , Student.gpa <= max_gpa).all()
        result = session.query(Student).filter(Student.gpa.between(min_gpa, max_gpa)).all()  #betmen🤣
    
    return result


def sorted_students_by_gpa(by: str = 'asc') -> list[Student]: # order_by default buyicha asc olar ekan pastdan terpaga desc esa tepadan 
    with get_db() as session:
        if by == 'asc':
           result = session.query(Student).order_by(Student.gpa.asc()) #pastdan tepaga 
        else:
           result = session.query(Student).order_by(Student.gpa.desc()) #tepadan pastga 

    return result

def add_scores(student_id: int , subject: str , ball: float ):
    with get_db() as session:
        student: Student = session.query(Student).get(student_id)
        student.scores.append(Score(subject=subject , ball=ball))
        session.commit()

def get_scores(student_id: int) ->list[Score]:
    with get_db() as session:
        student: Student = session.query(Student).get(student_id)
        return student.scores

def get_student_with_scores():
    with get_db() as session:
         students: list[Student] = session.query(Student).all()

         result= []
         for student in students:
            result.append({
                'student':student.full_name,
                'total_scores':len(student.scores)
            })

    return result