def correct_bracketing(brackets: str):
    counter = 0
    for bracket in brackets:
        if bracket == "<":
            counter += 1
        elif bracket == ">":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0
