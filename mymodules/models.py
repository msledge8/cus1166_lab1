class Student:

    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade

    def set_grade(self,student_grade):
        self.student_grade = student_grade

    def get_grade(self):
        return int(self.student_grade)

    def print_student_info(self):
        print(f"{self.student_name} got a {self.student_grade}.")

