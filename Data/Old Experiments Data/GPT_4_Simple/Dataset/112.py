def reverse_delete(s, c):
    result = ''.join([ch for ch in s if ch not in c])
    palindrome = result == result[::-1]
    return (result, palindrome)
