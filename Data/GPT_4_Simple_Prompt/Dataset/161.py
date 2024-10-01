def solve(s):
    # check if the string s contains any letters if not, reverse the string
    if not any(c.isalpha() for c in s):
        return s[::-1]
    else:
        # If letters are there in string, reverse its case
        return ''.join(c.lower() if c.isupper() else c.upper() for c in s)
