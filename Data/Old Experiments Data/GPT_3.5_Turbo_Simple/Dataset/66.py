def digitSum(s):
    upper_sum = sum(ord(char) for char in s if char.isupper())
    return upper_sum
