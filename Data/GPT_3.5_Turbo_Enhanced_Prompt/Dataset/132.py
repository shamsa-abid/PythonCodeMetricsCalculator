def is_nested(string):
    opening_brackets = 0
    closing_brackets = 0

    for bracket in string:
        if bracket == '[':
            opening_brackets += 1
        else:
            closing_brackets += 1

        if closing_brackets > opening_brackets:
            return True

    return False
