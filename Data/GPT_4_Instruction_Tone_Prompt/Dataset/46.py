def fib4(n: int):
    if n <= 3:
        return [0, 0, 2, 0][n]
    dp = [0, 0, 2, 0] + [0] * (n-3)
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
    return dp[n]
