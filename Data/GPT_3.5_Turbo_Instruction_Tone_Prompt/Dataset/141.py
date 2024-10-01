def file_name_check(file_name):
    if not isinstance(file_name, str):
        return 'No'

    if len([c for c in file_name if c.isdigit()]) > 3:
        return 'No'

    if '.' not in file_name or file_name.count('.') != 1:
        return 'No'

    file_parts = file_name.split('.')
    if len(file_parts) != 2:
        return 'No'

    if not file_parts[0] or not file_parts[0][0].isalpha():
        return 'No'

    if file_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
