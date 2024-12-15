from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if strings:
        return max(strings, key=len)
    return None
