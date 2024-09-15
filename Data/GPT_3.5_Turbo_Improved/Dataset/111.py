def histogram(test):
    dict1 = {}
    list1 = test.split()

    for letter in list1:
        dict1[letter] = dict1.get(letter, 0) + 1

    max_count = max(dict1.values())
    result = {key: value for key, value in dict1.items() if value == max_count}

    return result
