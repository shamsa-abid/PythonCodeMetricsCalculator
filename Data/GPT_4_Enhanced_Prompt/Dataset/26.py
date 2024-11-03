from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and numbers.count(num) == 1:
            result.append(num)
            seen.add(num)
    return result
