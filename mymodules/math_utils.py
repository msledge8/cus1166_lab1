from mymodules import models


def average_grade(roster):
    sum = 0
    for Student in roster:
        sum += Student.get_grade()
    print(f"The average is: {sum/len(roster)}.")
