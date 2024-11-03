def match_parens(lst):
    def check(s):
        balance = 0
        for p in s:
            balance += 1 if p == '(' else -1
            if balance < 0:
                return False
        return balance == 0

    return 'Yes' if check(lst[0] + lst[1]) or check(lst[1] + lst[0]) else 'No'
