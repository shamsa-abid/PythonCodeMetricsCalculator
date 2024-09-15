import re


def is_bored(S):
    boredoms = sum(1 for sentence in re.split(
        r'\s*[.?!]\s*', S) if sentence.startswith('I '))
    return boredoms
