def compare(game, guess):
    from itertools import starmap
    return list(starmap(lambda x, y: abs(x-y), zip(game, guess)))
