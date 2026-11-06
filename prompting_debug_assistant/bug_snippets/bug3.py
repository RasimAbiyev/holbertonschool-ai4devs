def get_student_name(students, index):
    return students[index]


students = ["Ali", "Leyla", "Murad", "Aysel"]

def display_student(students, index):
    name = get_student_name(students, index)
    print("Student name:", name)


display_student(students, 5)
