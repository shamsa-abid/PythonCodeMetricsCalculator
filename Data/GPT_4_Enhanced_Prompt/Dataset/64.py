def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(1 for c in s if c in vowels)
    if s and (s[-1] == 'y' or s[-1] == 'Y'):
        n_vowels += 1
    return n_vowels
