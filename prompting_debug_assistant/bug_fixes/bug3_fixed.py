students = ["Ali", "Leyla", "Murad", "Aysel"]


def get_student_name(student_list, index):
    if index < 0 or index >= len(student_list):
        return None
    return student_list[index]


def display_student(student_list, index):
    name = get_student_name(student_list, index)
    if name is None:
        print("Student not found")
    else:
        print("Student name:", name)


def main():
    print("Total students:", len(students))
    display_student(students, 2)


if __name__ == "__main__":
    main()
