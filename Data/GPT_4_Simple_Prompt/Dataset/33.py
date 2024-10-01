def sort_third(l):
    # Filter out the elements at indices divisible by three
    grouped_elements = [l[i] for i in range(len(l)) if i % 3 == 0]

    # Sort those elements
    sorted_elements = sorted(grouped_elements)

    # Insert the sorted elements back into the list at the correct positions
    for i, e in enumerate(sorted_elements):
        l[i * 3] = e

    return l
