def pairs_sum_to_zero(l):
    # Create a set to store the unique elements in the list
    unique_set = set(l)
    for num in unique_set:
        # If the negative counterpart of the current number exists in the set,
        # then we can conclude that there exist two numbers in the list whose sum is zero
        if -num in unique_set:
            return True
    return False
