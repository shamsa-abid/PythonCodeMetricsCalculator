def tri(n):
    sequence = [1, 3]
    if n == 0:
        return [1]
    elif n == 1:
        return sequence[:n+1]
    for i in range(2, n+1):
        if i % 2 == 0:
            sequence.append(sequence[-1] + 1)
        else:
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])
    return sequence
