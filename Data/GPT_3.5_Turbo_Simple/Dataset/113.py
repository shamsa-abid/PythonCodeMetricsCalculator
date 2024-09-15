def odd_count(lst):
    result = []
    for num_str in lst:
        odd_count = sum(1 for digit in num_str if int(digit) % 2 != 0)
        result.append(
            f"the number of odd elements {odd_count}n the str{odd_count}ng {num_str} of the {odd_count}nput.")
    return result
