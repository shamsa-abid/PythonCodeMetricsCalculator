def decode_shift(s: str):
    return "".join(chr((ord(ch) - 5 - 97) % 26 + 97) for ch in s)
