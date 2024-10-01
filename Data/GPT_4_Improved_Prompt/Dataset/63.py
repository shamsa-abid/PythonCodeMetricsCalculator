def fibfib(n):
    fibfib_values = [0, 0, 1] + [0] * (n - 2)
    for i in range(3, n + 1):
        fibfib_values[i] = fibfib_values[i - 1] + \
            fibfib_values[i - 2] + fibfib_values[i - 3]
    return fibfib_values[n]
