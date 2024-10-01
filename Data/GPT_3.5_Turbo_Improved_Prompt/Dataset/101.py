def words_string(s):
    if not s:
        return []

    s_list = s.replace(',', ' ').split()
    return s_list
