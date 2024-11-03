from typing import List


def sort_numbers(numbers: str) -> str:
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    numbers_list = numbers.split(' ')
    sorted_numbers = sorted(
        numbers_list, key=lambda x: value_map[x] if x in value_map else float('inf'))
    return ' '.join(sorted_numbers)
