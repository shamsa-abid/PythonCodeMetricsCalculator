def solve(s):
    new_str = []
    contains_letter = False
    for char in s:
        if char.isalpha():
            new_str.append(char.swapcase())
            contains_letter = True
        else:
            new_str.append(char)

    result = ''.join(new_str)

    if not contains_letter:
        return result[::-1]
    return result
