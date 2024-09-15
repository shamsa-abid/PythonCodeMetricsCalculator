def do_algebra(operator, operand):
    from operator import add, sub, mul, floordiv, pow
    operations_dict = {'+': add, '-': sub, '*': mul, '//': floordiv, '**': pow}

    result = operand[0]
    for oprt, oprn in zip(operator, operand[1:]):
        result = operations_dict[oprt](result, oprn)
    return result
