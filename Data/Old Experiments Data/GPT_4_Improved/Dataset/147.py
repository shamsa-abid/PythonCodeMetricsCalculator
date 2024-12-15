def get_max_triples(n):
    A = [i*i - i + 1 for i in range(1, n+1)]
    B = [0]*3
    B[1], B[2] = 1, 1
    ans = 0
    for i in range(3, n+1):
        ans += B[(3 - (i % 3) % 3) % 3]
        B[i % 3] += 1
    return ans
