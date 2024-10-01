def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack and stack[-1] == '[':
            stack.pop()

    return len(stack) < 2


# Test cases
print(is_nested('[[]]'))  # ➞ True
print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
print(is_nested('[][]'))  # ➞ False
print(is_nested('[]'))  # ➞ False
print(is_nested('[[][]]'))  # ➞ True
print(is_nested('[[]][['))  # ➞ True
