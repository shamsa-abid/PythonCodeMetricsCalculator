def how_many_times(string: str, substring: str) -> int:
    times = 0
    idx = 0
    while idx < len(string):
        idx = string.find(substring, idx)
        if idx == -1:
            break
        times += 1
        idx += 1

    return times
