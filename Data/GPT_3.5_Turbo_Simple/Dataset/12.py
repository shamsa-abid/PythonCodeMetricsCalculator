from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    max_length = len(strings[0])
    longest_str = strings[0]

    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            longest_str = s

    return longest_str
