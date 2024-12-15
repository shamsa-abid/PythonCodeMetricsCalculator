from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for group in paren_string.split():
        depth = max_depth = 0
        for c in group:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            max_depth = max(depth, max_depth)
        result.append(max_depth)
    return result
