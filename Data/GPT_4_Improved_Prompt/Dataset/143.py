from math import isqrt
def words_in_sentence(sentence):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    return ' '.join(word for word in sentence.split() if is_prime(len(word)))
