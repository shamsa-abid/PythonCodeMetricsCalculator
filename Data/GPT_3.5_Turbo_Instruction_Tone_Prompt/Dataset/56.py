def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0
