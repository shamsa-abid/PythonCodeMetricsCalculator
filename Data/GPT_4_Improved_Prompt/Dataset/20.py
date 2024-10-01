from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    closest_pair = min((numbers[i], numbers[i+1])
                       for i in range(len(numbers)-1))
    return closest_pair
