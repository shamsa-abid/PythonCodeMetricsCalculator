def odd_count(lst):
    result = []
    for i in lst:
        digits = [digit for digit in i]
        odd_digits = [digit for digit in digits if int(digit) % 2 != 0]
        odd_count = str(len(odd_digits))
        result.append("the number of odd elements " + odd_count + "n the str" +
                      odd_count + "ng " + odd_count + " of the " + odd_count + "nput.")
    return result
