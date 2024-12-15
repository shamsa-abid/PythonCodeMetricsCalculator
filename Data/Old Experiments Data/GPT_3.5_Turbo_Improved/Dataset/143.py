def words_in_sentence(sentence):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    new_lst = []
    for word in sentence.split():
        if is_prime(len(word)):
            new_lst.append(word)

    return " ".join(new_lst)