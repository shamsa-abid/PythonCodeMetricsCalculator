def even_odd_palindrome(n):
    even_pal = 0
    odd_pal = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_pal += 1
            else:
                odd_pal += 1
    return (even_pal, odd_pal)
