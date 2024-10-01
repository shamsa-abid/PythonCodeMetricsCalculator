def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
    else:
        return ''.join(char.swapcase() if char.isalpha() else char for char in s)
