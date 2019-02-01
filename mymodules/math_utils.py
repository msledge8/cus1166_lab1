from mymodules import models


def average_grade(roster):
    sum = 0
    for Student in roster:
        sum += Student.get_grade()

    if (sum/len(roster) > 89):
        letter = "A"
    elif (sum/len(roster) > 79):
        letter = "B"
    elif (sum/len(roster) > 69):
        letter = "C"
    elif (sum/len(roster) > 59):
        letter = "D"
    else:
        letter = "F"
    print(f"The average is: {sum/len(roster)}. The average letter grade was {letter}.")
