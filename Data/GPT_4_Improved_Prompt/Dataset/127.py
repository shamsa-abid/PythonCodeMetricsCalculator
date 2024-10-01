def intersection(interval1, interval2):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    l, r = max(interval1[0], interval2[0]), min(interval1[1], interval2[1])
    return "YES" if r - l > 0 and is_prime(r - l) else "NO"
