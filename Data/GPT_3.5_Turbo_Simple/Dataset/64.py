def vowels_count(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            if s[i].lower() == 'y' and i != len(s)-1:
                continue
            count += 1
    return count
