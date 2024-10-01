def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    # Checking if the last character is alphabetical
    if txt[-1].isalpha():
        # Checking if the last character is not part of a word
        if len(txt) == 1 or txt[-2] == ' ':
            return True
    return False


# Test cases
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False
