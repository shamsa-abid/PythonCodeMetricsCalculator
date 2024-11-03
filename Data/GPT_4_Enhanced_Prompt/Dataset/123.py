def get_odd_collatz(n):
    collatz_list = []

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            collatz_list.append(n)
            n = n * 3 + 1
    collatz_list.append(1)

    collatz_list.sort()

    return collatz_list
