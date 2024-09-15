import re


def valid_date(date):
    pattern = re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
    if pattern.match(date):
        month, day, year = [int(i) for i in date.split('-')]
        if month < 1 or month > 12 or day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2 and day > 29:
            return False
        return True
    else:
        return False
