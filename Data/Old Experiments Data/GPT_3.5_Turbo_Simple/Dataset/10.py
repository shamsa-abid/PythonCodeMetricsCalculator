def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    if not string:
        return ''

    i = len(string) - 1
    while i >= 0:
        if string[:i + 1] == string[:i + 1][::-1]:
            break
        i -= 1

    return string + string[:i][::-1]


# Test cases
print(make_palindrome(''))
print(make_palindrome('x'))
print(make_palindrome('xyz'))
print(make_palindrome('xyx'))
print(make_palindrome('jerry'))
