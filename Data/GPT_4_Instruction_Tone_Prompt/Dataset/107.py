def even_odd_palindrome(n):
    even = 0
    odd = 0

    # Helper function to check if a number is palindrome
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2:
                odd += 1
            else:
                even += 1

    return (even, odd)
