
def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append("(")
        elif bracket == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return len(stack) == 0


# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
