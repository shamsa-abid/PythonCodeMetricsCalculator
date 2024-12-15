def correct_bracketing(brackets: str):
    depth = 0

    for bracket in brackets:
        depth += 1 if bracket == '<' else -1
        if depth < 0:
            return False

    return depth == 0
