def vowels_count(s):
    count = sum(1 for char in s.lower() if char in 'aeiou')
    if s.lower().endswith('y'):
        count += 1
    return count