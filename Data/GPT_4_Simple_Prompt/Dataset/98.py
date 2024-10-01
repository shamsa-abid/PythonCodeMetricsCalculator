def count_upper(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):   # iterate through even indices of string
        if s[i] in vowels:
            count += 1
    return count
