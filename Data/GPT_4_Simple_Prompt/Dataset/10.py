def is_palindrome(string: str) -> bool:
    """Test if a string is a palindrome"""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with the supplied string by
    finding the longest postfix of the supplied string that is a palindrome and then
    appending to the end of the string the reverse of the string prefix that comes before
    the palindrome suffix.
    """
    # If the string is empty or a palindrome, return the string itself
    if not string or is_palindrome(string):
        return string

    # Finding the longest palindromic suffix
    for i in range(len(string), 0, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            # If we found a palindrome, add to the end of the string the reverse of the remaining prefix
            return string + string[:i][::-1]

