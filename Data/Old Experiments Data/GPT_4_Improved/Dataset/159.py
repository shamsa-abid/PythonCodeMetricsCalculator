def eat(number, need, remaining):
    eaten = min(need, remaining) + number
    remaining = max(0, remaining - need)
    return [eaten, remaining]
