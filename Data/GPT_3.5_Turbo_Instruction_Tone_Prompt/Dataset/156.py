
def int_to_mini_roman(number):
    if not isinstance(number, int) or number < 1 or number > 1000:
        return "Invalid input"

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["m", "cm", "d", "cd", "c", "xc",
            "l", "xl", "x", "ix", "v", "iv", "i"]
    roman_numeral = ''
    index = 0
    while number > 0:
        if number - val[index] >= 0:
            roman_numeral += syms[index]
            number -= val[index]
        else:
            index += 1
    return roman_numeral.lower()
