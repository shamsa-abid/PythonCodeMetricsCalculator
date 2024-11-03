
def fruit_distribution(s, n):
    nums = [int(i) for i in s.split() if i.isdigit()]
    return n - sum(nums)
