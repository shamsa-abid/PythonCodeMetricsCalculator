def valid_date(date):
    # check if the date string is not empty
    if not date:
        return False

    # split the date string into parts
    parts = date.split('-')

    # check if there are 3 parts
    if len(parts) != 3:
        return False

    month, day, year = parts

    # check if month is a number between 1 and 12
    if not month.isdigit() or not 1 <= int(month) <= 12:
        return False

    # check if day is a number between 1 and 31 based on the month
    if not day.isdigit():
        return False
    day = int(day)
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if not 1 <= day <= 31:
            return False
    elif month in ['04', '06', '09', '11']:
        if not 1 <= day <= 30:
            return False
    else:
        # February
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
            if not 1 <= day <= 29:
                return False
        else:
            if not 1 <= day <= 28:
                return False

    # check if year is a 4-digit number
    if len(year) != 4 or not year.isdigit():
        return False

    return True


# Test cases
print(valid_date('03-11-2000'))  # Output: True
print(valid_date('15-01-2012'))  # Output: False
print(valid_date('04-0-2040'))  # Output: False
print(valid_date('06-04-2020'))  # Output: True
print(valid_date('06/04/2020'))  # Output: False
