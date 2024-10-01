
def string_xor(a: str, b: str) -> str:
    result = ''
    for char1, char2 in zip(a, b):
        result += '1' if char1 != char2 else '0'
    return result
