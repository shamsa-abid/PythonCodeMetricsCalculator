def car_race_collision(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input should be a non-negative integer.")
    return n * n
