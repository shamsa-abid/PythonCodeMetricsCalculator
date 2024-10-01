def is_bored(S):
    sentences = [sentence.strip() for sentence in re.split('[.!?]', S)]
    count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            count += 1
    return count
