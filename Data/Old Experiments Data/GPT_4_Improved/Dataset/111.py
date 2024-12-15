def histogram(test):
    from collections import Counter

    # Count frequency of each word
    frequency_dict = Counter(test.split())

    # Find the max frequency
    max_freq = max(frequency_dict.values(), default=0)

    # Filter dictionary by max frequency and return
    return {key: value for key, value in frequency_dict.items() if value == max_freq}
