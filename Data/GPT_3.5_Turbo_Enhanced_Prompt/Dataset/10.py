def make_palindrome(string: str) -> str:
    if not string:
        return ''

    suffix_length = 0
    while string[suffix_length:] != string[suffix_length:][::-1]:
        suffix_length += 1

    palindrome_suffix = string[suffix_length:]
    return string + palindrome_suffix[::-1]
