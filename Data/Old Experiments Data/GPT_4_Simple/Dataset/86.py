def anti_shuffle(s):
    # split the string into list of words
    words = s.split(" ")

    # initial empty result string
    res = ''

    # loop through each word
    for word in words:
        # sort the words based on ascii value
        sorted_word = ''.join(sorted(word))

        # append sorted words to result string with space
        res += sorted_word + " "

    # removing the last extra space
    res = res.rstrip()

    return res
