def vowels_count(s):
    vowels = "aeiouAEIOU"
    s = s.lower()
    return sum(map(s.count, vowels)) + int(s.endswith('y'))
