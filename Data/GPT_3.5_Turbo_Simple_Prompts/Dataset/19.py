
from typing import List


def sort_numbers(numbers: str) -> str:
    num_mapping = {'zero': 0, 'one': 1, 'two': 2, 'three': 3,
                   'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    def convert_number(number_str):
        return num_mapping[number_str]

    number_list = numbers.split()
    number_list.sort(key=convert_number)

    return ' '.join(number_list)


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
