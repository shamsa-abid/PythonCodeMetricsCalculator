def solve(N):
    binary_sum = sum(int(x) for x in bin(N)[2:])
    return bin(binary_sum)[2:]
