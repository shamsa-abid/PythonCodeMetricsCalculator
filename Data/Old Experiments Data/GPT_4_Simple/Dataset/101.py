def words_string(s):
    s = s.replace(",", " ")
    return list(filter(None, s.split(" ")))
