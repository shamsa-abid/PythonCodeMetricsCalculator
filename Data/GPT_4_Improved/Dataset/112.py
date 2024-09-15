def reverse_delete(s, c):
    s = s.translate({ord(i): None for i in c})
    return (s, s == s[::-1])
