from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_numbers = []
    for num in numbers:
        if numbers.count(num) == 1:
            unique_numbers.append(num)
    return unique_numbers


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
