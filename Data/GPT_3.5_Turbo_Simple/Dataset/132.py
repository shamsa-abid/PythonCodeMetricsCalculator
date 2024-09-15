def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack:
            stack.pop()
    # If stack is not empty, return True, else return False.
    return bool(stack)
