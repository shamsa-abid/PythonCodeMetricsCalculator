def correct_bracketing(brackets: str):
    counter = 0
    for char in brackets:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
            if counter < 0:
                return False
    return counter == 0
