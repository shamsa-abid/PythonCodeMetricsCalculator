def is_palindrome(text: str):
    return text == text[::-1]  # Check if the text is equal to its reverse


# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
