def count_distinct_characters(string: str) -> int:
    # convert the string to lowercase to ignore case sensitivity
    string = string.lower()

    # create a set to store unique characters
    unique_chars = set()

    # iterate through the characters in the string
    for char in string:
        # add the character to the set
        unique_chars.add(char)

    # return the length of the set, which gives the count of distinct characters
    return len(unique_chars)


# test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
