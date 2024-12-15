def even_odd_count(num):
    num = str(abs(num))
    odd_count = sum(1 for digit in num if int(digit) % 2)
    even_count = len(num) - odd_count
    return even_count, odd_count
