def even_odd_palindrome(n):
    n = min(n, 1000)
    even_count, odd_count = 0, 0
    for num in range(1, n+1):
        s = str(num)
        if s == s[::-1]:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
