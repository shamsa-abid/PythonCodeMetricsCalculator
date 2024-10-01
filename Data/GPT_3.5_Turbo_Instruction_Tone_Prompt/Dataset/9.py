
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]

    for i in range(1, len(numbers)):
        rolling_max_list.append(max(numbers[i], rolling_max_list[i-1]))

    return rolling_max_list
