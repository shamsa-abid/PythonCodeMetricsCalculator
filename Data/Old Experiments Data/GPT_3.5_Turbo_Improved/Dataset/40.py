def triples_sum_to_zero(l: list):
    seen = set()

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            complement = -(l[i] + l[j])
            if complement in seen:
                return True
            seen.add(l[j])

    return False
