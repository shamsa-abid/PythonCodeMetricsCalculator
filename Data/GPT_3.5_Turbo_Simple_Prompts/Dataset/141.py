def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'

    name, extension = file_name.split('.')

    if not name or not name[0].isalpha():
        return 'No'

    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    if sum(char.isdigit() for char in name) > 3:
        return 'No'

    return 'Yes'
