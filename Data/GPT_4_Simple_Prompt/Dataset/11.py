def string_xor(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    return ''.join('1' if ai != bi else '0' for ai, bi in zip(a, b))
