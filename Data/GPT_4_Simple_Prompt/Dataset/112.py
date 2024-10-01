def reverse_delete(s, c):
    s = ''.join(ch for ch in s if ch not in c)
    return (s, s == s[::-1])
