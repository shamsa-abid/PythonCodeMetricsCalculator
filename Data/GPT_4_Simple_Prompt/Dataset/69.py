def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    from collections import Counter
    # count the occurences of each number
    counter = Counter(lst)
    # sort numbers in descending order
    for num in sorted(counter, reverse=True):
        # if the number's frequency is >= it's value
        if counter[num] >= num:
            return num
    # if no such number exists, return -1
    return -1
