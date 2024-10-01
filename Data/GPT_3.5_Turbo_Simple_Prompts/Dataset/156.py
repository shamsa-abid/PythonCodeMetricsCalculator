def int_to_mini_roman(number):
    if not isinstance(number, int) or number < 1 or number > 1000:
        return "Input must be a positive integer between 1 and 1000"

    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
        90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    result = ""
    for key in sorted(roman_numerals.keys(), reverse=True):
        while number >= key:
            result += roman_numerals[key]
            number -= key

    return result.lower()


# Test cases
print(int_to_mini_roman(19))  # Output: 'xix'
print(int_to_mini_roman(152))  # Output: 'clii'
print(int_to_mini_roman(426))  # Output: 'cdxxvi'
