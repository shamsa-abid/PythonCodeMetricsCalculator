from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:

    # Using list comprehension to generate the resultant list
    result = [x for n in numbers for x in (n, delimiter)][:-1]

    return result
