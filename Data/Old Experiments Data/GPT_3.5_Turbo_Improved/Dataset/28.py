
from typing import List


def concatenate(strings: List[str]) -> str:
    if strings:
        return ''.join(strings)
    else:
        return ''
