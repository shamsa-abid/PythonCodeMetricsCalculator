def solve(N):
    return format(sum(int(digit) for digit in bin(N)[2:]), 'b')
