def even_odd_palindrome(n):
    def is_palindrome(x): return str(x) == str(x)[::-1]
    palindrome_nums = [i for i in range(1, n+1) if is_palindrome(i)]
    even = sum(1 for i in palindrome_nums if i % 2 == 0)
    odd = sum(1 for i in palindrome_nums if i % 2 != 0)
    return (even, odd)
