import operator as op
def do_algebra(operators, operands):
    operations = {'+': op.add, '-': op.sub,
                  '*': op.mul, '//': op.floordiv, '**': op.pow}
    result = operands[0]
    for operator, operand in zip(operators, operands[1:]):
        result = operations[operator](result, operand)
    return result
