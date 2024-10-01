def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # sort the array first
    closest = (numbers[0], numbers[1])  # initialize the closest pair
    # initialize the minimum difference
    min_difference = numbers[1] - numbers[0]

    # iterate over the list from index 1 to length - 1
    for i in range(1, len(numbers)-1):
        difference = numbers[i+1] - numbers[i]
        if difference < min_difference:  # if the difference between two numbers is less than minimum difference so far
            min_difference = difference
            closest = (numbers[i], numbers[i+1])  # update the closest pair

    return closest
