def match_parens(lst):
    v1 = lst[0].count(')') <= lst[1].count('(')
    v2 = lst[1].count(')') <= lst[0].count('(')
    v3 = lst[0].count(')') == lst[0].count('(')
    v4 = lst[1].count(')') == lst[1].count('(')
    if (v1 or v2) and not (v3 and v4):
        return 'Yes'
    else:
        return 'No'
