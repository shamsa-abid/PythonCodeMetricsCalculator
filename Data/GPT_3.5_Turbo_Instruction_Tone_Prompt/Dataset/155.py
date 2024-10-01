def even_odd_count(num):
    even_count = sum(1 for x in str(abs(num)) if int(x) % 2 == 0)
    odd_count = sum(1 for x in str(abs(num)) if int(x) % 2 != 0)
    return (even_count, odd_count)
