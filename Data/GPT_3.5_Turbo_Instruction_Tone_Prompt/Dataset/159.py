def eat(number, need, remaining):
    total_eaten = number + need
    remaining -= need
    if remaining < 0:
        remaining = 0
    return [total_eaten, remaining]
