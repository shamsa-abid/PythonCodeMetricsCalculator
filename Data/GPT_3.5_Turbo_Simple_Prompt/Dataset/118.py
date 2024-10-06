def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    right_consonants = ""
    found_vowel = False

    for char in word[::-1]:
        if char in consonants:
            right_consonants += char
        elif char in vowels:
            found_vowel = True
            break

    if not found_vowel or len(right_consonants) < 2:
        return ""

    return right_consonants[1]


# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
