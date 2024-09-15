def even_odd_count(num):
    even_count = sum(1 for i in str(abs(num)) if int(i) % 2 == 0)
    odd_count = sum(1 for i in str(abs(num)) if int(i) % 2 != 0)
    return (even_count, odd_count)
