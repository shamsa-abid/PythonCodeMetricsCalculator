def valid_date(date):
    if not date:
        return False
    if len(date) != 10:
        return False
    if date[2] != "-" or date[5] != "-":
        return False

    split_date = date.split("-")

    try:
        month, day, year = int(split_date[0]), int(
            split_date[1]), int(split_date[2])
    except ValueError:
        return False

    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if len(str(year)) != 4:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if day > 29:
            return False
        elif day == 29:
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                return False

    return True
