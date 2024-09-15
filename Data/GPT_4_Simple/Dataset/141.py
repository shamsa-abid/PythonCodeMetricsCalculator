def file_name_check(file_name):
    import re
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.[txtedll]*$', file_name):
        return 'No'
    if len(re.findall('\d', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
