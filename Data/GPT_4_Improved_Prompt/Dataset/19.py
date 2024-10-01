from typing import List

VALUE_MAP = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
             'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def sort_numbers(numbers: str) -> str:
    words = numbers.split()
    words_sorted = sorted(words, key=lambda x: VALUE_MAP[x])
    return ' '.join(words_sorted)
