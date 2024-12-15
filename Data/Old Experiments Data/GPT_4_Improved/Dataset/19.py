def sort_numbers(numbers: str) -> str:
    number_word_to_value_map = {
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

    number_words = numbers.split(' ')
    sorted_numbers = sorted(number_words, key=number_word_to_value_map.get)

    return ' '.join(sorted_numbers)
