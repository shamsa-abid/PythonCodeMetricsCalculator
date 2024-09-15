import hashlib


def string_to_md5(text):
    if text:
        return hashlib.md5(text.encode('ascii')).hexdigest()
    else:
        return None
