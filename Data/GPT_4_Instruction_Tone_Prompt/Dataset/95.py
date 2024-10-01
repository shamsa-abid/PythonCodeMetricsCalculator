def check_dict_case(dict):
    if not dict:
        return False
    keys = dict.keys()
    upper_case_keys = [key for key in keys if isinstance(
        key, str) and key.isupper()]
    lower_case_keys = [key for key in keys if isinstance(
        key, str) and key.islower()]
    return (len(upper_case_keys) == len(keys)) or (len(lower_case_keys) == len(keys))
