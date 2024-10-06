def add(lst):
    even_sum = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum


# Test the function with the provided example
print(add([4, 2, 6, 7]))
