def words_in_sentence(sentence):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    split_sentence = sentence.split(" ")
    primes = [word for word in split_sentence if is_prime(len(word))]
    return " ".join(primes)