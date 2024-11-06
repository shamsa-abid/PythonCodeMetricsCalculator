from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        depths.append(max_depth)

    return depths