def digitSum(s: str) -> int:
    return sum(ord(i) for i in s if i.isupper())
