def count_nums(arr):
    def sum_digits(n):
        """
        Helper function to calculate the sum of digits for a given number.
        Uses the fact that converting a number to a string reveals its digits,
        which can then be easily summed.
        """
        return sum(int(digit) for digit in str(abs(n)))

    return sum(1 for number in arr if sum_digits(number) > 0)
