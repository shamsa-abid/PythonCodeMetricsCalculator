def histogram(test):
    test = test.split()
    frequency_dict = {item: test.count(item) for item in test}
    max_val = max(frequency_dict.values()) if frequency_dict else 0
    return {key: val for key, val in frequency_dict.items() if val == max_val}
