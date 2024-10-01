def file_name_check(file_name):
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1
    if digit_count > 3:
        return 'No'

    try:
        name, extension = file_name.split('.')
    except ValueError:
        return 'No'

    if len(name) == 0 or not name[0].isalpha():
        return 'No'

    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
