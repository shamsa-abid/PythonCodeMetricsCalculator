def make_palindrome(string: str) -> str:
    length = len(string)
    last_char_index = length - 1
    while last_char_index >= 0:
        if is_palindrome(string[0:last_char_index + 1]):
            break
        last_char_index -= 1
    return string + string[:last_char_index + 1][::-1]


def is_palindrome(string: str) -> bool:
    return string == string[::-1]
