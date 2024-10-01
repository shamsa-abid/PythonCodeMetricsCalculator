
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    max_length = max(len(s) for s in strings)
    longest_strings = [s for s in strings if len(s) == max_length]

    return longest_strings[0]
