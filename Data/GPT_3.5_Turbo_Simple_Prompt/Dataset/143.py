def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def words_in_sentence(sentence):
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)


# Example Usage
sentence1 = "This is a test"
print(words_in_sentence(sentence1))  # Output: "is"

sentence2 = "lets go for swimming"
print(words_in_sentence(sentence2))  # Output: "go for"
