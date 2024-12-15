def solve(N):
    return bin(sum(map(int, str(bin(N)[2:]))))[2:]
