from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    running_max = numbers[0]
    result = [running_max]

    for n in numbers[1:]:
        running_max = max(running_max, n)
        result.append(running_max)

    return result
