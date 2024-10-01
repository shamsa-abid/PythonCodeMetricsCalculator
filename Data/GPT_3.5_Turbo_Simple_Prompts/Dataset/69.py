def search(lst):
    frequency_dict = {}

    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    max_num = -1
    for num, freq in frequency_dict.items():
        if num > freq and freq >= num:
            max_num = max(max_num, num)

    return max_num


# Examples
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
