def reverse_delete(s, c):
    s = ''.join([char for char in s if char not in c])
    is_palindrome = s == s[::-1]
    return s, is_palindrome


# Test cases
print(reverse_delete("abcde", "ae"))  # ('bcd', False)
print(reverse_delete("abcdef", "b"))  # ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # ('cdedc', True)
