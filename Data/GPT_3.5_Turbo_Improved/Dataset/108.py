def count_nums(arr):
    def digits_sum(n):
        neg = 1 if n >= 0 else -1
        n = [int(i) for i in str(abs(n))]
        n[0] *= neg
        return sum(n)

    return len([x for x in arr if digits_sum(x) > 0]) if arr else 0
