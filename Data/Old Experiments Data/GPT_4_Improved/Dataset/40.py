def triples_sum_to_zero(l: list):
    l = sorted(l)
    for i in range(len(l)-2):
        if i > 0 and l[i] == l[i-1]:
            continue

        left, right = i+1, len(l)-1
        while left < right:
            total = l[i] + l[left] + l[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                return True
                left += 1
                right -= 1

    return False
