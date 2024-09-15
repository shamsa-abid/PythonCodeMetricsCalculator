def check_dict_case(dict):
    if not dict:
        return False
    is_lower = all(k.islower() for k in dict if isinstance(k, str))
    is_upper = all(k.isupper() for k in dict if isinstance(k, str))
    return is_lower or is_upper
