import re
def fix_spaces(text):
    text = re.sub(' {3,}', '-', text)
    text = re.sub(' ', '_', text)
    return text
