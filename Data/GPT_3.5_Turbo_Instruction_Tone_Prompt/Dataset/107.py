def even_odd_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    count_even = 0
    count_odd = 0

    for num in range(1, n+1):
        if is_palindrome(num):
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

    return (count_even, count_odd)
