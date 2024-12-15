def digitSum(s):
    if not s:
        return 0
    return sum(ord(char) for char in s if char.isupper())
