def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        if char == ']':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    count_open = string.count('[')
    count_close = string.count(']')

    return count_open > 1 and count_close > 1
