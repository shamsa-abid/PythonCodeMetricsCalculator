
def solve(s):
    new_str = [i.swapcase() if i.isalpha() else i for i in s]
    if not any(char.isalpha() for char in s):
        return s[::-1]
    return ''.join(new_str)
