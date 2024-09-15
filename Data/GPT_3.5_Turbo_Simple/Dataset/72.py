def will_it_fly(q, w):
    def is_palindromic(lst):
        return lst == lst[::-1]

    if is_palindromic(q) and sum(q) <= w:
        return True
    else:
        return False
