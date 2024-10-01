def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary."""

    # sum of digits of binary representation of N
    sum_of_digits = bin(N)[2:].count('1')

    return bin(sum_of_digits)[2:]


print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"
