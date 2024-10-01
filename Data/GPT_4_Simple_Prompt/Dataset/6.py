def parse_nested_parens(paren_string):
    groups = paren_string.split()
    result = []
    for group in groups:
        max_depth, cur_depth = 0, 0
        for c in group:
            if c == '(':
                cur_depth += 1
            elif c == ')':
                cur_depth -= 1
            max_depth = max(max_depth, cur_depth)
        result.append(max_depth)
    return result
