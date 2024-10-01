def eat(number, need, remaining):
    total_eaten = number + min(remaining, need)
    remaining = max(0, remaining - need)
    return [total_eaten, remaining]
