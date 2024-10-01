def get_max_triples(n):
    cnt = [0] * 3
    result = 0
    for i in range(1, n + 1):
        result += cnt[(3 - i % 3) % 3]
        cnt[i % 3] += 1
    return result
