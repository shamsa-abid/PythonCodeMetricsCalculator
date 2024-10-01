def reverse_delete(s, c):
    char_set = set(c)
    s = ''.join([char for char in s if char not in char_set])
    return s, s == s[::-1]
