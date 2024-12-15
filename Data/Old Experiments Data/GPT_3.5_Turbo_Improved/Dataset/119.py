def check(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()

    return not stack


def match_parens(lst):
    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]

    return 'Yes' if check(S1) or check(S2) else 'No'
