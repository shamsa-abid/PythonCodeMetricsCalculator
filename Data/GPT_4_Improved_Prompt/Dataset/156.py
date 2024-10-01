def int_to_mini_roman(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['m', 'cm', 'd', 'cd', 'c', 'xc',
               'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    roman = ''
    for i in range(len(values)):
        while number >= values[i]:
            roman += symbols[i]
            number -= values[i]
    return roman

