from typing import List


def concatenate(strings: List[str]) -> str:
    if not strings:
        return ''

    return ''.join(strings)
