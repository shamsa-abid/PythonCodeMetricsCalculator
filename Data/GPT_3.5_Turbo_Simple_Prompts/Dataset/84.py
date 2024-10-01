def solve(N):
    binary_sum = 0
    while N > 0:
        binary_sum += N % 2
        N = N // 2
    return bin(binary_sum)[2:]


# Test cases
print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"
