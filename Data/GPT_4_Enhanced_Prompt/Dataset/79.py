def decimal_to_binary(decimal):
    binary = '{0:b}'.format(decimal)
    return "db" + binary + "db"
