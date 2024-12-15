def vowels_count(s):
    s = s.lower()
    count = [each for each in "aeiou" for c in s if c == each]
    if s.endswith('y'):
        count.append('y')
    return len(count)
