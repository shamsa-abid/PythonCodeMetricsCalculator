def odd_count(lst):
    result = []
    for num_str in lst:
        odd_count = sum(1 for digit in num_str if int(digit) % 2 != 0)
        result.append(
            f"the number of odd elements {odd_count}n the str{odd_count}ng {num_str} of the {num_str}nput.")
    return result


# Test cases
print(odd_count(['1234567']))
print(odd_count(['3', '11111111']))
