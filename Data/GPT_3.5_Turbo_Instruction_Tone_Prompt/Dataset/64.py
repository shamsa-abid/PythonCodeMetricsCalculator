
def vowels_count(s):
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        elif i == len(s) - 1 and s[i] == 'y':
            count += 1

    return count
