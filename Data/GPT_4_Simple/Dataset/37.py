def sort_even(l):
    even = sorted([l[i] for i in range(0, len(l), 2)])
    out = []
    j = 0
    for i in range(len(l)):
        if i % 2 == 0:
            out.append(even[j])
            j += 1
        else:
            out.append(l[i])
    return out
