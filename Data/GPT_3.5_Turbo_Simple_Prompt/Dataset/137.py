def compare_one(a, b):
    if type(a) == type(b):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(float(a), float(b))
    else:
        a = a.replace(",", ".") if isinstance(a, str) else float(a)
        b = b.replace(",", ".") if isinstance(b, str) else float(b)
        return max(a, b)


# Test cases
print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None
