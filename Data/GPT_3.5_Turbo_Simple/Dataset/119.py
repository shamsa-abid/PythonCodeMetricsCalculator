def match_parens(lst):
    stack = []
    mapping = {')': '('}

    for s in lst:
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return 'No'

    return 'Yes' if not stack else 'No'
