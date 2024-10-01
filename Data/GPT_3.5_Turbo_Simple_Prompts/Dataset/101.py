def words_string(s):
    words = s.replace(",", " ").split()
    return words


# Test cases
# Output: ["Hi", "my", "name", "is", "John"]
print(words_string("Hi, my name is John"))
# Output: ["One", "two", "three", "four", "five", "six"]
print(words_string("One, two, three, four, five, six"))
