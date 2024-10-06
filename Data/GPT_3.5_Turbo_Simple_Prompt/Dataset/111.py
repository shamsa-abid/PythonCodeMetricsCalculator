def histogram(test):
    if test == "":
        return {}

    test_list = test.split()
    count_dict = {}

    for letter in test_list:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

    max_count = max(count_dict.values())
    result = {key: value for key, value in count_dict.items() if value ==
              max_count}

    return result
