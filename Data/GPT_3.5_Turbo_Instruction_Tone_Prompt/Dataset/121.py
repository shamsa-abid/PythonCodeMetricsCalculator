def solution(lst):
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 != 0) if len(lst) > 1 else 0
