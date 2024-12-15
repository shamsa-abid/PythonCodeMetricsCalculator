def count_nums(arr):
    return len([i for i in arr if sum(int(c) for c in str(abs(i))) > 0])
