def numerical_letter_grade(grades):
    grade_boundaries = [0.0, 0.7, 1.0, 1.3,
                        1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]
    letter_grades = ["E", "D-", "D", "D+", "C-",
                     "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
    letter_grade = []
    for gpa in grades:
        for index in range(len(grade_boundaries) - 1, -1, -1):
            if gpa >= grade_boundaries[index]:
                letter_grade.append(letter_grades[index])
                break
    return letter_grade
