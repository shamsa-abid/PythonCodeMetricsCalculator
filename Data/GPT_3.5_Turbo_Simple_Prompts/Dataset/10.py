def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """

    def longest_palindromic_suffix_length(s):
        for i in range(len(s), 0, -1):
            if is_palindrome(s[:i]):
                return i
        return 0

    longest_suffix_len = longest_palindromic_suffix_length(string)
    return string + string[:len(string) - longest_suffix_len][::-1]


# Testing the function
print(make_palindrome(''))  # Output: ''
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
