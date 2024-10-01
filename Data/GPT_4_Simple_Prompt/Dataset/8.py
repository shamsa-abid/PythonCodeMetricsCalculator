def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if len(numbers) == 0:
        return (0, 1)
    else:
        # Sum of numbers
        sum_num = sum(numbers)

        # Product of numbers
        prod_num = 1
        for num in numbers:
            prod_num *= num

        return (sum_num, prod_num)
