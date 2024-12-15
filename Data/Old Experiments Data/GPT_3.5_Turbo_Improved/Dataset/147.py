def get_max_triples(n):
    A = [i*i - i + 1 for i in range(1, n+1)]
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (A[i]+A[j]+A[k]) % 3 == 0:
                    ans += 1
    return ans
