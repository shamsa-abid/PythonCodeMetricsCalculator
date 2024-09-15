def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def words_in_sentence(sentence):
    words = sentence.split(' ')
    prime_word = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_word)
