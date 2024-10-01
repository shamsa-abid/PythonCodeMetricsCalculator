def histogram(test):
    from collections import Counter
    # Split the input string into a list of letters (remove spaces)
    letters = [l for l in test.split() if l.isalpha()]
    # Count the occurrence of each letter
    counts = Counter(letters)
    # Find the maximum occurrence
    max_occurrence = max(counts.values()) if counts else 0
    # Select letters with the maximum occurrence
    max_letters = {k: v for k, v in counts.items() if v == max_occurrence}
    return max_letters
