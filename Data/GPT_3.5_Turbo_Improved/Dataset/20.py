from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            new_distance = abs(numbers[i] - numbers[j])
            if distance is None or new_distance < distance:
                distance = new_distance
                closest_pair = (min(numbers[i], numbers[j]), max(
                    numbers[i], numbers[j]))

    return closest_pair
