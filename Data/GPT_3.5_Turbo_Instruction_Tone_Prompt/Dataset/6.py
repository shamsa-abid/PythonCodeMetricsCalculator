
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    depth = 0

    for char in paren_string:
        if char == '(':
            depth += 1
            depths.append(depth)
        elif char == ')':
            depth -= 1

    return [max(depths) if depth > 0 else 0 for depth in depths if depth > 0]
