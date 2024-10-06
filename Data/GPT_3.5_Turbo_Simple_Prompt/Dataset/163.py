
def generate_integers(a, b):
    result = []
    start = min(a, b)
    end = max(a, b)

    while start <= end:
        if start % 2 == 0:
            result.append(start)
        start += 1

    return result


# Test cases
print(generate_integers(2, 8))  # Output: [2, 4, 6, 8]
print(generate_integers(8, 2))  # Output: [2, 4, 6, 8]
print(generate_integers(10, 14))  # Output: []
