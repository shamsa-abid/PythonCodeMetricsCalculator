
def vowels_count(s):
    count = 0
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

    for i in range(len(s)):
        if s[i].lower() in vowels:
            if s[i].lower() == 'y' and i != len(s) - 1:
                continue
            count += 1

    return count


# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("sky"))    # Output: 1
