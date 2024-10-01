def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # if strings is empty return None
        return None
    # find the string in the list with maximum length
    longest_str = max(strings, key=len)
    return longest_str
