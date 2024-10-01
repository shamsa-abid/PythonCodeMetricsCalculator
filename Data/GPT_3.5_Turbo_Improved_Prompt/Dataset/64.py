
def vowels_count(s):
    vowels = "aeiouy"
    n_vowels = sum(1 for c in s if c.lower() in vowels)
    return n_vowels
