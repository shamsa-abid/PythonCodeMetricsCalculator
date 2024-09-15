import hashlib


def string_to_md5(text):
    return None if not text else hashlib.md5(text.encode()).hexdigest()
