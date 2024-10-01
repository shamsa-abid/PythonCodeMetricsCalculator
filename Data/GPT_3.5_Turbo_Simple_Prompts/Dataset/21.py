from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)

    scaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return scaled_numbers


# Test the function with the example from the docstring
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
