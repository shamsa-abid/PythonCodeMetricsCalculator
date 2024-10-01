def file_name_check(file_name):
    import re

    # check more than three digits ('0'-'9') in the file's name or not
    if len(re.findall("\d", file_name)) > 3:
        return 'No'

    # check if file's name contains exactly one dot '.' or not
    if file_name.count(".") != 1:
        return 'No'

    # split file_name into two parts
    base, ext = file_name.rsplit(".", 1)

    # check the substring before the dot should not be empty, and it starts with a letter from the latin alphabet
    if not base or not base[0].isalpha() or not base.isalnum():
        return 'No'

    # check the substring after the dot is one of these: ['txt', 'exe', 'dll'] or not
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
