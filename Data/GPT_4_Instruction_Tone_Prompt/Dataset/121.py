def solution(lst):
    return sum([num for index, num in enumerate(lst) if index % 2 == 0 and num % 2 == 1])
