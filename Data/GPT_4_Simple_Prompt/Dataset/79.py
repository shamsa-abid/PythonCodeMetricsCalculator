def decimal_to_binary(decimal):
    # convert decimal to binary and remove the '0b' prefix
    binary = bin(decimal)[2:]
    return 'db' + binary + 'db'  # add 'db' at the beginning and end of the string
