def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            s = 0
            for j in range(1, i+1):
                s += j
            result.append(s)
    return result


# Test the function with example
print(f(5))  # Output: [1, 2, 6, 24, 15]
