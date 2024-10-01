from collections import Counter


def histogram(test):
    count_dict = Counter(test.split())
    max_count = max(count_dict.values(), default=0)
    return {k: v for k, v in count_dict.items() if v == max_count}
