def is_bored(S):
    boredoms = 0
    sentences = S.split('.')
    sentences = [sentence.strip()
                 for sentence in sentences if sentence.strip()]

    for sentence in sentences:
        words = sentence.split()
        if len(words) > 0 and words[0] == "I":
            boredoms += 1

    return boredoms


# Test cases
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
