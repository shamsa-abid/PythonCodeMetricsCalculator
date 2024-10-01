def odd_count(lst):
    out = []
    for i in lst:
        cnt = sum([1 for d in i if int(d) % 2])
        out.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(
            cnt, cnt, cnt, cnt))
    return out
