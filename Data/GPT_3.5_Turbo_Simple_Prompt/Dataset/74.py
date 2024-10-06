def total_match(lst1, lst2):
    total_chars_lst1 = sum(map(len, lst1))
    total_chars_lst2 = sum(map(len, lst2))

    if total_chars_lst1 == total_chars_lst2:
        return lst1
    elif total_chars_lst1 < total_chars_lst2:
        return lst2
    else:
        return lst1


# Test the function with the provided examples
print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
# ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']
