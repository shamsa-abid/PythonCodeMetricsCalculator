def solve(N):
    binary_num = bin(N)[2:]
    binary_sum = binary_num.count('1')
    return bin(binary_sum)[2:]
