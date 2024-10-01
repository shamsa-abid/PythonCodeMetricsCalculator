def file_name_check(file_name):
    suffixes = ['txt', 'exe', 'dll']
    parts = file_name.split('.')

    if len(parts) != 2:
        return 'No'

    name, ext = parts

    if ext not in suffixes:
        return 'No'

    if len(name) == 0 or not name[0].isalpha():
        return 'No'

    if sum(1 for char in name if char.isdigit()) > 3:
        return 'No'

    return 'Yes'
