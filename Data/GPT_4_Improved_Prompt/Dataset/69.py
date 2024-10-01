from collections import Counter


def search(lst):
    freq_dict = Counter(lst)
    max_freq_num = max(
        (num for num, freq in freq_dict.items() if freq >= num), default=-1)
    return max_freq_num
