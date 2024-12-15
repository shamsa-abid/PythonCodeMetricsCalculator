def triples_sum_to_zero(l: list):
    l.sort()
    for i in range(len(l)-2):
        left, right = i+1, len(l)-1
        while left < right:
            sum = l[i] + l[left] + l[right]
            if sum == 0:
                return True
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return False
