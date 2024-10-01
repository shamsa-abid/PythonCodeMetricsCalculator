def Strongest_Extension(class_name, extensions):
    def extension_strength(extension):
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        return cap - sm
    strongest = max(extensions, key=extension_strength)
    return f'{class_name}.{strongest}'
