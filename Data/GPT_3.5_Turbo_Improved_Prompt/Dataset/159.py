def eat(number, need, remaining):
    eaten = number + min(need, remaining)
    left = max(remaining - need, 0)
    return [eaten, left]
