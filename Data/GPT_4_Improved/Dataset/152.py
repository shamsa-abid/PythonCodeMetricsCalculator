def compare(game, guess):
    return list(map(lambda x, y: abs(x-y), game, guess))
