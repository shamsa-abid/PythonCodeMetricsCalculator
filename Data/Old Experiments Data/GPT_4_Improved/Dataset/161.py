def solve(s):
    return ''.join([i.swapcase() if i.isalpha() else i for i in s])[::-1] if not any(i.isalpha() for i in s) else ''.join([i.swapcase() if i.isalpha() else i for i in s])
