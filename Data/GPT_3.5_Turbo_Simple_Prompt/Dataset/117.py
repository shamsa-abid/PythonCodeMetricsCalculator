def select_words(s, n):
    def count_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        count = 0
        for letter in word:
            if letter in consonants:
                count += 1
        return count

    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result


# Test cases
print(select_words("Mary had a little lamb", 4))  # ["little"]
print(select_words("Mary had a little lamb", 3))  # ["Mary", "lamb"]
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ["world"]
print(select_words("Uncle sam", 3))  # ["Uncle"]
