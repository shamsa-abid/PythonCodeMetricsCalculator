def Strongest_Extension(class_name, extensions):
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for letter in extension if letter.isupper())
        sm = sum(1 for letter in extension if letter.islower())
        strength = cap - sm

        if strength > max_strength:
            strongest_extension = extension
            max_strength = strength

    return f"{class_name}.{strongest_extension}"


# Example
# Output: 'my_class.AA'
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
