def solve(N):
    binary_sum = sum(int(i) for i in str(N))
    return bin(binary_sum)[2:]
