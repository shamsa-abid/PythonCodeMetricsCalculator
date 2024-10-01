def eat(number, need, remaining):
    eat = min(need, remaining)
    number += eat
    remaining -= eat
    return [number, remaining]
