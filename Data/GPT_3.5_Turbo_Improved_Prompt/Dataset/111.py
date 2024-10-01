def histogram(test):
    dict1 = {}
    list1 = test.split()

    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    max_occurrence = max(dict1.values())
    result = {key: val for key, val in dict1.items() if val == max_occurrence}

    return result
