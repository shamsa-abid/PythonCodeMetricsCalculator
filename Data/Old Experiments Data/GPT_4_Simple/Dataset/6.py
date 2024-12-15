from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    max_depths = []
    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
            elif char == ')':
                if current_depth > max_depth:
                    max_depth = current_depth
                current_depth -= 1
        max_depths.append(max_depth)
    return max_depths
