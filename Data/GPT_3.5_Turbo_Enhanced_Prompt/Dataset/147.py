
def get_max_triples(n):
    count = 0
    for i in range(1, n + 1):
        remainder = (i * i - i + 1) % 3
        if remainder == 0:
            count += i // 2
        elif remainder == 1:
            count += (i - 1) // 2
        else:
            count += i // 2
    return count
