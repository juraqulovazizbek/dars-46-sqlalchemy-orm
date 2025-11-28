from datetime import date
from school.create_tables import init_db
from school.crud import (
    create_student,
    get_students,
    get_one_student,
    search_students_by_first_name,
    search_students_by_name,
    update_student , 
    filter_students_by_gender ,
    filter_students_by_gpa, 
    sorted_students_by_gpa,
    add_scores,
    get_scores , 
    get_student_with_scores,
    generate_certificate_code
)

init_db()


# create_student('ali', 'valiyev3', date(2005, 9, 3))

# students = get_students()
# print(students)

# s = get_one_student(1)
# print(s.bio)

# sts = search_students_by_first_name('ali')
# print(sts)

# sts = search_students_by_name('vali')
# print(sts)

# update_student(1, last_name='nimadir')

# females = filter_students_by_gender('Female')
# for female in females:
#     print(female.full_name, '->' ,female.gender)

# gpa = filter_students_by_gpa(3, 3.2)
# for g in gpa:
#     print(g.gpa , g.full_name)

# gpa = sorted_students_by_gpa('asc')
# for g in gpa:
#     print(g.gpa , g.full_name)


# add_scores(13 , 'math' , 3)

# for i in get_student_with_scores():
#     print(i)

# print(get_student_with_scores()[12])





# --- Simple Tests ---
# 1. Create student test
print(create_student("Test", "User", date(2000,1,1)))


# 2. Get all students test
print(get_students())


# 3. Add score test
add_scores(1, "Math", 5)


# 4. Print student with scores
print(get_student_with_scores())