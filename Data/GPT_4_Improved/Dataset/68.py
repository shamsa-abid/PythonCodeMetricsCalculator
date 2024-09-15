def pluck(arr):
    try:
        min_value, min_index = min(
            ((v, i) for i, v in enumerate(arr) if v % 2 == 0),
            default=([],)
        )
        return [min_value, min_index]
    except ValueError:
        return []
