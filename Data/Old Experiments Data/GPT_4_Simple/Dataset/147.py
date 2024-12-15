def get_max_triples(n):
    # Create the integer array.
    a = [i * i - i + 1 for i in range(1, n + 1)]

    # Count the numbers congruent to 0, 1, and 2 modulo 3.
    counts = [0, 0, 0]
    for num in a:
        counts[num % 3] += 1

    # Calculate the number of triples.
    triples = counts[0] * (counts[0] - 1) * (counts[0] - 2) // 6 + \
        counts[1] * counts[2] * (counts[2] - 1) // 2 + \
        counts[2] * counts[1] * (counts[1] - 1) // 2

    return triples
