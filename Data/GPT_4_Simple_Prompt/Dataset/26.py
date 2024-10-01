def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result
