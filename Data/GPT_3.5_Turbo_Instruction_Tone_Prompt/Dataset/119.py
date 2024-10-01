
def match_parens(lst):
    total_open = 0
    for s in lst:
        for paren in s:
            if paren == '(':
                total_open += 1
            else:
                if total_open == 0:
                    return 'No'
                total_open -= 1
    return 'Yes'
