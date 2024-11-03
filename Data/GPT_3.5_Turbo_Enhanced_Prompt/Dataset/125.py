
import string


def split_words(txt):
    # Check for whitespaces
    if " " in txt:
        return [word for word in txt.split()]
    # Check for commas
    elif "," in txt:
        return [word for word in txt.replace(',', ' ').split()]
    else:
        # Count number of lower-case letters with odd order in the alphabet
        return len([char for char in txt if char.islower() and char in string.ascii_lowercase[1::2]])
