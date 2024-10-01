def fizz_buzz(n: int):
    count = 0
    for i in range(n):
        if i % 77 == 0 or i % 143 == 0:
            count += str(i).count('7')
    return count
