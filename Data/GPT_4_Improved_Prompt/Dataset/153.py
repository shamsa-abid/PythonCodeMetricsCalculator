def Strongest_Extension(class_name, extensions):
    strengths = [(e, sum(1 for c in e if c.isupper()) -
                  sum(1 for c in e if c.islower())) for e in extensions]
    strongest_extension = max(strengths, key=lambda x: x[1])[0]
    return f'{class_name}.{strongest_extension}'
