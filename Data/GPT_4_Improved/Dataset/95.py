def check_dict_case(dict):
    keys = list(dict.keys())
    if not keys:
        return False

    if all(isinstance(i, str) and i.isupper() for i in keys):
        return True
    if all(isinstance(i, str) and i.islower() for i in keys):
        return True

    return False
