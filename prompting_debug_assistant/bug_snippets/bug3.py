students = ["Ali", "Leyla", "Murad", "Aysel"]


def get_student_name(student_list, index):
    name = student_list[index]
    return name


def display_student(student_list, index):
    name = get_student_name(student_list, index)
    print("Student name:", name)


def main():
    print("Total students:", len(students))
    display_student(students, 5)


main()
