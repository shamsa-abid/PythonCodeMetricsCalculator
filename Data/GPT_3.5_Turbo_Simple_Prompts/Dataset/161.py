def solve(s):
    new_s = ''
    has_letter = False

    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                new_s += char.upper()
            else:
                new_s += char.lower()
        else:
            new_s += char

    if not has_letter:
        new_s = new_s[::-1]

    return new_s


# Test cases
print(solve("1234"))  # Output: "4321"
print(solve("ab"))    # Output: "AB"
print(solve("#a@C"))  # Output: "#A@c"
