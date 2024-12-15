def make_palindrome(string: str) -> str:
    if not string:
        return ''

    suffix = ''
    for i in range(len(string), 0, -1):
        if string[:i] == string[:i][::-1]:
            suffix = string[i:]
            break

    return string + suffix[::-1]
