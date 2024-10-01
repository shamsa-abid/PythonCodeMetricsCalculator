from typing import List
from collections import Counter


def remove_duplicates(numbers: List[int]) -> List[int]:
    counter = Counter(numbers)
    return [n for n in numbers if counter[n] == 1]
