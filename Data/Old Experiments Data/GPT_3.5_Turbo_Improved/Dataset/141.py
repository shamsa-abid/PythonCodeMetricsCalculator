def file_name_check(file_name):
    suffixes = ['txt', 'exe', 'dll']
    parts = file_name.split('.')

    if len(parts) != 2:
        return 'No'

    name, ext = parts[0], parts[1]

    if len(name) == 0 or not name[0].isalpha() or len([char for char in name if char.isdigit()]) > 3:
        return 'No'

    if ext not in suffixes:
        return 'No'

    return 'Yes'
