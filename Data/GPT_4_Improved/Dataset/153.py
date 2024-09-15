def Strongest_Extension(class_name, extensions):
    def strength(ext): return sum(1 if c.isupper()
                                  else -1 for c in ext if c.isalpha())
    return class_name + '.' + max(extensions, key=strength)
