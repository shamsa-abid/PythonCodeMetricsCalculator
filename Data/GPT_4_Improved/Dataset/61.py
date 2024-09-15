def correct_bracketing(brackets: str) -> bool:
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        elif b == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0
