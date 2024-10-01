def count_nums(arr):
    return sum([1 for i in arr if sum(int(d) for d in str(abs(i))) > 0])
