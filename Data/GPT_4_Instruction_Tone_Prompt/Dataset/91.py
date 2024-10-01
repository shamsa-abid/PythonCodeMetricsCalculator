def is_bored(S):
    # Separate the sentences
    sentences = S.replace("?", ".").replace("!", ".").split(".")
    # Count the boredoms
    return sum(1 for sentence in sentences if sentence.strip().startswith('I'))
