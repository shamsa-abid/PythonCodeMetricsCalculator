def tri(n):
    tribonacci = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            tribonacci.append(i / 2 + 1)
        else:
            tribonacci.append(tribonacci[i - 1] +
                              tribonacci[i - 2] + (i + 3) / 2)
    return tribonacci
