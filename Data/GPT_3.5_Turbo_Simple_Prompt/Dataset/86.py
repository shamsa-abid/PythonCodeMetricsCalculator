def anti_shuffle(s):
    def order_string(word):
        return ''.join(sorted(word))

    words = s.split()
    ordered_words = [order_string(word) for word in words]
    return ' '.join(ordered_words)


# Test cases
print(anti_shuffle('Hi'))  # Output: 'Hi'
print(anti_shuffle('hello'))  # Output: 'ehllo'
print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'
