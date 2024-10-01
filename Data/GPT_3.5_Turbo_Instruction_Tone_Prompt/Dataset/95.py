
def check_dict_case(dict):
    if not dict:
        return False

    lower_case_keys = all(isinstance(key, str) and key.islower()
                          for key in dict.keys())
    upper_case_keys = all(isinstance(key, str) and key.isupper()
                          for key in dict.keys())

    return lower_case_keys or upper_case_keys
