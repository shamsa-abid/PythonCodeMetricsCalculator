def eat(number, need, remaining):
    eaten = number
    if remaining >= need:
        eaten += need
        remaining -= need
    else:
        eaten += remaining
        remaining = 0
    return [eaten, remaining]
