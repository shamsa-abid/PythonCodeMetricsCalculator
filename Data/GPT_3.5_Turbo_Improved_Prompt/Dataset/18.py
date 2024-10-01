def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0

    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += 1

    return count
