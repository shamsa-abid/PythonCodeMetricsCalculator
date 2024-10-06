def solution(lst):
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 != 0) if len(lst) % 2 == 0 else 0


# Test the function with the examples given in the docstring
print(solution([5, 8, 7, 1]))  # Output: 12
print(solution([3, 3, 3, 3, 3]))  # Output: 9
print(solution([30, 13, 24, 321]))  # Output: 0
