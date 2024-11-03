def make_palindrome(string: str) -> str:
    for i in range(len(string)-1, -1, -1):
        if string[i:] == string[i:][::-1]:
            break
    return string+string[:i][::-1]
