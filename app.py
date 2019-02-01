from mymodules.models import Student
from mymodules.math_utils import average_grade

def __main__():
    roster = []
    roster.append(Student("Hermione", "100"))
    roster.append(Student("Harry", "88"))
    roster.append(Student("Ron", "78"))
    roster.append(Student("Luna", "90"))
    roster.append(Student("Neville", "81"))
    roster.append(Student("Draco", "91"))
    roster.append(Student("Dean", "80"))
    roster.append(Student("Lavender", "78"))
    roster.append(Student("Crabbe", "60"))
    roster.append(Student("Goyle", "61"))

    for student in roster:
        student.print_student_info()

    average_grade(roster)

__main__()




