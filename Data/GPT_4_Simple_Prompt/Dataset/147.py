def get_max_triples(n):
    a = [i*i - i + 1 for i in range(1, n+1)]
    cnt = [0]*3
    res = 0

    for num in a:
        res += cnt[-num % 3]
        cnt[num % 3] += 1

    return res
