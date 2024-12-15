def even_odd_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    even_count = sum(1 for i in range(1, n+1) if i %
                     2 == 0 and is_palindrome(i))
    odd_count = sum(1 for i in range(1, n+1) if i %
                    2 == 1 and is_palindrome(i))

    return (even_count, odd_count)
