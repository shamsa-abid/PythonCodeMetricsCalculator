def int_to_mini_roman(number):
    value_map = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"),
                 (90, "xc"), (50, "l"), (40, "xl"), (10, "x"),
                 (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]

    roman_num = ""

    for i, numeral in value_map:
        while number >= i:
            roman_num += numeral
            number -= i
    return roman_num
