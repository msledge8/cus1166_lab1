def average_grade(roster):
    sum = 0
    for student in roster:
        if (student.get_grade == "A"):
            sum += 4
        elif (student.get_grade == "B"):
            sum += 3
        elif (student.get_grade == "C"):
            sum += 2
        elif (student.get_grade == "D"):
            sum += 1
        else:
            sum += 0

    return (sum/len(roster))
