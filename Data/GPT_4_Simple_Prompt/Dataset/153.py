def Strongest_Extension(class_name, extensions):
    # Calculate the strength of each extension and create a list of tuples in
    # the format: (extension, strength)
    extensions_strength = [(ext_name, sum(
        [1 if ch.isupper() else -1 for ch in ext_name])) for ext_name in extensions]

    # Sort the list of tuples based on strength in descending order.
    # In case of a tie, the extension that comes first in the list will stay first due to Python's stable sorting.
    extensions_strength.sort(key=lambda x: x[1], reverse=True)

    # Return the name of the class concatenated with the name of the strongest extension.
    return f'{class_name}.{extensions_strength[0][0]}'
