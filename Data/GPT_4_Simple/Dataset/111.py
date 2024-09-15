def histogram(test):
    test = test.split()
    counted_letters = {i: test.count(i) for i in test}
    max_value = max(counted_letters.values())

    return {k: v for k, v in counted_letters.items() if v == max_value}
