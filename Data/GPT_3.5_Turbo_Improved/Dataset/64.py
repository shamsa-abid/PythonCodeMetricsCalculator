def vowels_count(s):
    vowels = "aeiouyAEIOUY"
    n_vowels = sum(1 for c in s if c in vowels)
    return n_vowels

