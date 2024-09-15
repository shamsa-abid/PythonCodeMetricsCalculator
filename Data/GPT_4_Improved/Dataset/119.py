def match_parens(lst):
    def balance(s): return all(s.count(i) == s.count(j)
                               for i, j in zip('(', ')))'))
    S1, S2 = lst[0] + lst[1], lst[1] + lst[0]
    return 'Yes' if balance(S1) or balance(S2) else 'No'
