def triples_sum_to_zero(l: list):
    seen = set()
    for i in range(len(l)):
        num1 = l[i]
        for j in range(i + 1, len(l)):
            num2 = l[j]
            target = - (num1 + num2)
            if target in seen:
                return True
            seen.add(num1)
            seen.add(num2)
    return False
