def cycpattern_check(a, b):
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0]  # rotate the second word
    return False


# Test cases
print(cycpattern_check("abcd", "abd"))  # False
print(cycpattern_check("hello", "ell"))  # True
print(cycpattern_check("whassup", "psus"))  # False
print(cycpattern_check("abab", "baa"))  # True
print(cycpattern_check("efef", "eeff"))  # False
print(cycpattern_check("himenss", "simen"))  # True
