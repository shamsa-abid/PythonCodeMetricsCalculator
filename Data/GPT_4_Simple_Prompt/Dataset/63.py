def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        dp = [0, 0, 1] + [0]*(n-2)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
