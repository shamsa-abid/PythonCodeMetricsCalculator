def prime_fib(n: int) -> int:
    def is_prime(num):  # check if a number is prime
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    def fibonacci(n):  # returns n-th fibonacci number
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    count = 0
    fib_num = 0

    while count < n:
        if is_prime(fibonacci(fib_num)):
            count += 1
            if count == n:
                return fibonacci(fib_num)
        fib_num += 1
