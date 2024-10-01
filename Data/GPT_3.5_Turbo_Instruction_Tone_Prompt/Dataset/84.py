
def solve(N):
    binary_sum = bin(N)[2:]
    total_sum = str(sum(int(digit) for digit in binary_sum))
    return total_sum
