student_grades = {  }

def add_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"added {name} with a {grade}")


def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade

        print(f"{name} with marks are update {grade}")

    else:
        print(f"{name} is not found!")


def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successful deleted")
    else:
        print(f"{name} is not found")


def display_all_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print("no student found/added")


