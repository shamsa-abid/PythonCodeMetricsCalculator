def Strongest_Extension(class_name, extensions):
    strength_list = []
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        strength_list.append(strength)
    strongest_extension = extensions[strength_list.index(max(strength_list))]
    return class_name + '.' + strongest_extension
