def file_name_check(file_name):
    valid_extensions = {'txt', 'exe', 'dll'}
    name, sep, ext = file_name.partition('.')

    if sep != '.' or not name or ext not in valid_extensions or not name[0].isalpha():
        return 'No'

    if sum(ch.isdigit() for ch in name) > 3:
        return 'No'

    return 'Yes'
