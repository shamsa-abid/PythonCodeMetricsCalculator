def sort_numbers(numbers: str) -> str:
    number_words = ['zero', 'one', 'two', 'three',
                    'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: number_words.index(x))
    return ' '.join(numbers_list)
