def match_parens(lst):
    a = lst[0].count('(')-lst[0].count(')')
    b = lst[1].count('(')-lst[1].count(')')

    # check the first '('
    if a >= 0 and b+a >= 0:
        return 'Yes'

    # check the first ')'
    elif a < 0 and b-a >= 0:
        return 'Yes'

    else:
        return 'No'
