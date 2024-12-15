from typing import List


def concatenate(strings: List[str]) -> str:
    if not strings:
        return ''
    elif all(isinstance(i, str) for i in strings):
        return ''.join(strings)
    else:
        raise ValueError("All elements in the list must be strings")
