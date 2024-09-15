def correct_bracketing(brackets: str):
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")" and stack:
            stack.pop()
        else:
            return False
    return len(stack) == 0
