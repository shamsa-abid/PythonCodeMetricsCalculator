def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_pair = (numbers[0], numbers[1])
    min_distance = abs(numbers[1] - numbers[0])

    for i in range(2, len(numbers)):
        distance = abs(numbers[i] - numbers[i-1])
        if distance < min_distance:
            min_distance = distance
            min_pair = (numbers[i-1], numbers[i])

    return min_pair
