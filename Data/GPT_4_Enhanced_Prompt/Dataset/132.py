def is_nested(string):
    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        if string[i] == ']':
            count -= 1
        if count < 0:
            return False
    return count == 0 if string.count("[") == 1 else True
