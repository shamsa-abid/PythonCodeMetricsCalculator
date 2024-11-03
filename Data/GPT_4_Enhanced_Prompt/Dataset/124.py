
import re


def valid_date(date):
    try:
        month, day, year = [int(i) for i in re.split('-', date.strip())]
        day_limits = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if 1 <= month <= 12 and 1 <= day <= day_limits[month - 1]:
            return True
        return False
    except ValueError:
        return False
