def solve(N):
    return format(sum(int(digit) for digit in str(N)), 'b')
