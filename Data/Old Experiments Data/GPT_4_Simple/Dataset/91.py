import re
def is_bored(S):
    sentences = [sentence.strip() for sentence in re.split('[.!?]', S)]
    return len([sentence for sentence in sentences if sentence.startswith('I')])
