def int_to_mini_roman(num):
    if not 1 <= num <= 1000:
        raise ValueError("Out of range: num should be within 1 to 1000")

    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC",
            "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''

    for i in range(len(vals)):
        count = int(num / vals[i])
        roman += syms[i] * count
        num -= vals[i] * count

    return roman.lower()