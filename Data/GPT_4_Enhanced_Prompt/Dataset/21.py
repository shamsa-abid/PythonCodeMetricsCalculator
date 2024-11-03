from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Check if the number list is empty or contain only one value
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Compute the min and max in a single pass for better performance
    max_number = max_number = numbers[0]
    for num in numbers[1:]:
        if num < min_number:
            min_number = num
        elif num > max_number:
            max_number = num

    # Check if all numbers in the list are the same
    if min_number == max_number:
        raise ValueError(
            "All numbers in the list are the same, cannot rescale")

    diff = max_number - min_number
    return [(x - min_number) / diff for x in numbers]
