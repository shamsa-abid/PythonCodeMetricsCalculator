def histogram(test):
    histogram_dict = {}
    for letter in test.split():
        if letter in histogram_dict:
            histogram_dict[letter] += 1
        else:
            histogram_dict[letter] = 1

    max_occurrence = max(histogram_dict.values())
    result = {key: value for key, value in histogram_dict.items()
              if value == max_occurrence}

    return result
