def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions."""
    return sum(i for index, i in enumerate(lst) if i % 2 != 0 and index % 2 == 0)
