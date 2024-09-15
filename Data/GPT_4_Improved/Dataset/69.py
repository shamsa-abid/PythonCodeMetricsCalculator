def search(lst):
    from collections import Counter
    count = Counter(lst)
    result = -1
    for key, val in count.items():
        if key <= val:
            result = max(result, key)
    return result
