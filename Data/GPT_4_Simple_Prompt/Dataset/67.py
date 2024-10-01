import re
def fruit_distribution(s, n):
    num_list = re.findall('\d+', s)
    apples, oranges = map(int, num_list)
    mangoes = n - apples - oranges
    return mangoes
