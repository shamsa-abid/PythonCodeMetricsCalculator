def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3,
                    'four': 4, 'five': 5, 'six': 6, 'seven': 7,
                    'eight': 8, 'nine': 9}

    reverse_numeral_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
                            4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                            8: 'eight', 9: 'nine'}

    number_list = numbers.split()
    number_list = [numeral_dict[number] for number in number_list]
    number_list.sort()
    number_list = [reverse_numeral_dict[number] for number in number_list]

    return ' '.join(number_list)
