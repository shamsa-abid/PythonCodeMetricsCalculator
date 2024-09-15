def count_upper(s):
    vowel_set = set("AEIOU")
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowel_set)
