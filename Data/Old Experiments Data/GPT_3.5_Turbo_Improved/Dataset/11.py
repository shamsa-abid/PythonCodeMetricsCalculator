
def string_xor(a: str, b: str) -> str:
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))
