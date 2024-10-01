def vowels_count(s):
    s = s.lower()
    count = 0
    vowels = 'aeiou'
    for i in s:
        if i in vowels:
            count += 1
    if s.endswith('y'):
        count += 1
    return count
