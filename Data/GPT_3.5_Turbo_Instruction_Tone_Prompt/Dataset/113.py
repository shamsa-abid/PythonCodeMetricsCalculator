def odd_count(lst):
    result = []
    for string in lst:
        count = sum(int(digit) % 2 != 0 for digit in string)
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(
            count, count, count, count))
    return result
