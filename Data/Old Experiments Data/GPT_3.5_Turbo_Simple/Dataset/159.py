def eat(number, need, remaining):
    total_eaten = number + need
    if remaining >= need:
        remaining -= need
    else:
        total_eaten += remaining
        remaining = 0
    return [total_eaten, remaining]
