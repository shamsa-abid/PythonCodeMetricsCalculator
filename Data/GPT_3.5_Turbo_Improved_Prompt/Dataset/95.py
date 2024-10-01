def check_dict_case(dict):
    keys = dict.keys()

    if len(keys) == 0:
        return False

    is_lower = all(isinstance(key, str) and key.islower() for key in keys)
    is_upper = all(isinstance(key, str) and key.isupper() for key in keys)

    return is_lower or is_upper
