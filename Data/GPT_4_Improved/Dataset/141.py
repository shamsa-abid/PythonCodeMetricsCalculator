def file_name_check(file_name):
    file_parts = file_name.split('.')

    if (len(file_parts) != 2 or
        not file_parts[1] in ['txt', 'exe', 'dll'] or
        not file_parts[0] or
        not file_parts[0][0].isalpha() or
            sum(c.isdigit() for c in file_parts[0]) > 3):
        return 'No'

    return 'Yes'
