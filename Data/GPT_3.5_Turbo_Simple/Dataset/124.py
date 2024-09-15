def valid_date(date):
    if not date:
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False

    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2 and (day < 1 or day > 29):
        return False

    return True
