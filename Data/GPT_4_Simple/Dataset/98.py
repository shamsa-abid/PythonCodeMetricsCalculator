def count_upper(s):
    return sum(1 for i, letter in enumerate(s) if i % 2 == 0 and letter in 'AEIOU')
