from typing import List


def triples_sum_to_zero(l: List[int]) -> bool:
    l.sort()
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        left, right = i + 1, len(l) - 1
        while left < right:
            total = l[i] + l[left] + l[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                return True
    return False
