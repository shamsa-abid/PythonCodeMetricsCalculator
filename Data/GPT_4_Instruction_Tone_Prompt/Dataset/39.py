def prime_fib(n: int) -> int:
    import math

    def check_prime(num):
        if num > 1:
            for i in range(2, int(math.sqrt(num))+1):
                if (num % i) == 0:
                    return False
            return True
        else:
            return False

    def nth_prime_fib(n):
        count = 0
        fib = [0, 1]
        i = 2
        while count < n:
            fib.append(fib[i-1] + fib[i-2])
            if check_prime(fib[i]):
                count += 1
            i += 1
        return fib[i - 1]

    return nth_prime_fib(n)
