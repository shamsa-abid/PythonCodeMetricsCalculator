def search(lst):
    counts = {x: lst.count(x) for x in list(set(lst))}
    result = [k for k in counts.keys() if k <= counts[k]]
    return max(result) if result else -1