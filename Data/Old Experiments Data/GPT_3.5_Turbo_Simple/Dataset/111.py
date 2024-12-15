def histogram(test):
    result = {}
    test_list = test.split()

    for letter in test_list:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    max_count = max(result.values())
    final_result = {key: value for key,
                    value in result.items() if value == max_count}

    return final_result
