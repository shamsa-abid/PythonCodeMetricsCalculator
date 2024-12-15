from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    try:
        return list(filter(lambda x: substring in x, strings))
    except TypeError:
        return []
