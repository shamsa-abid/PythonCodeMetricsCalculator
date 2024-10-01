def select_words(s, n):
    # List of vowels in English alphabet
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Split the input string into words
    words = s.split(" ")

    # List to store the words with exactly n consonants
    n_cons_words = []

    # Iterate over the words in the given string
    for word in words:
        # Convert the word to lowercase and assign to a new variable
        w = word.lower()
        # Initialize a counter for consonants
        cons_count = 0
        # Iterate over the characters in the word
        for char in w:
            if char not in vowels:
                # If the character is not a vowel, increment the consonant count
                cons_count += 1
        # If the count of consonants in the word is equal to n, add the word to the result list
        if cons_count == n:
            n_cons_words.append(word)
    # Return the list of words with exactly n consonants
    return n_cons_words
