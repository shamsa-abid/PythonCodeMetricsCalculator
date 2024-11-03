def count_upper(s):
    count = sum(1 for i in range(1, len(s), 2) if s[i] in "AEIOU")
    return count
