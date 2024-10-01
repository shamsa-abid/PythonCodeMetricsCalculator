def digitSum(s):
    return sum(ord(char) for char in s if char.isupper()) if s else 0
