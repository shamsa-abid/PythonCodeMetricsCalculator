def count_nums(arr):
    def get_sum_of_digits(num):
        if num < 0:
            num = -num
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        return sum_digits

    count = 0
    for num in arr:
        if get_sum_of_digits(num) > 0:
            count += 1

    return count
