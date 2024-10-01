def tri(n):
    ans = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            ans.append(1 + i / 2)
        else:
            ans.append(sum(ans[-1:-4:-1]))
    return ans
