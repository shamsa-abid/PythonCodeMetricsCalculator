def correct_bracketing(brackets: str):

    depth = 0

    # Iterate over every character in brackets
    for bracket in brackets:

        # Increment if opening bracket is encountered
        if bracket == "<":
            depth += 1

        # Decrement if closing bracket is encountered
        elif bracket == ">":

            # Return false if closing bracket appears without matching opening bracket
            if depth == 0:
                return False
            else:
                depth -= 1

     # Check if all brackets are balanced
    return depth == 0
