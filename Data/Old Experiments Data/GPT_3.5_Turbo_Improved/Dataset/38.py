def decode_cyclic(s: str):
    def decode_group(group):
        return group[-1] + group[:-1]

    groups = [s[(3*i):min((3*i + 3), len(s))] for i in range((len(s) + 2)//3)]
    decoded_groups = [decode_group(group) if len(
        group) == 3 else group for group in groups]
    return "".join(decoded_groups)
