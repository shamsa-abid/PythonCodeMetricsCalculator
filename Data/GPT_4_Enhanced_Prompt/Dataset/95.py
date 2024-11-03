def check_dict_case(d):
    if not d:
        return False
    is_uppercase = all(k.isupper() for k in d if isinstance(k, str))
    is_lowercase = all(k.islower() for k in d if isinstance(k, str))
    has_non_strings = any(not isinstance(k, str) for k in d)
    return (is_uppercase or is_lowercase) and not has_non_strings
