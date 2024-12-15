def is_nested(string):
    open_count = close_count = nesting = 0
    for char in string:
        if char == "[":
            open_count += 1
        elif char == "]":
            if open_count > close_count:
                close_count += 1
                if open_count > close_count:
                    nesting += 1
        else:
            return False
    return nesting >= 1 and open_count == close_count
