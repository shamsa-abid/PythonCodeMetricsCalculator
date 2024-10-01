def search(lst):
    frequency_dict = {}
    for num in lst:
        if num > 0:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

    result = -1
    for key, value in frequency_dict.items():
        if key > 0 and key <= value:
            result = max(result, key)

    return result
