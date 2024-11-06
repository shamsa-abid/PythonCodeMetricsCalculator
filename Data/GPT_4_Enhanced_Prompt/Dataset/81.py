def numerical_letter_grade(grades):
    GRADE_SCALE = [(4.0, 'A+'), (3.7, 'A'), (3.3, 'A-'), (3.0, 'B+'),
                   (2.7, 'B'), (2.3, 'B-'), (2.0, 'C+'), (1.7, 'C'),
                   (1.3, 'C-'), (1.0, 'D+'), (0.7, 'D'), (0.0, 'D-'),
                   (0.0, 'E')]

    letter_grades = []
    for gpa in grades:
        for value, grade in GRADE_SCALE:
            if gpa >= value:
                letter_grades.append(grade)
                break
    return letter_grades