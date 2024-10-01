def is_bored(S):
    boredoms = 0
    sentences = S.split(".")+S.split("?")+S.split("!")
    for sentence in sentences:
        if sentence.strip().startswith("I"):
            boredoms += 1
    return boredoms
