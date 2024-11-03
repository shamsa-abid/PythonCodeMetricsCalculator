def count_nums(arr):
    def digit_sum(n):
        neg = 1
        if n < 0:
            n, neg = -n, -1
        return sum(int(i) for i in str(n)) * neg

    return sum(1 for num in arr if digit_sum(num) > 0)
