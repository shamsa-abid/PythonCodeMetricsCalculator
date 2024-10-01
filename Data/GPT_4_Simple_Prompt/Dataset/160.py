def do_algebra(operator, operand):
    try:
        if len(operator) != len(operand)-1:
            raise ValueError(
                "The length of operator list must be equal to the length of operand list minus one.")
        result = operand[0]
        for i in range(len(operator)):
            if operator[i] == '+':
                result += operand[i+1]
            elif operator[i] == '-':
                result -= operand[i+1]
            elif operator[i] == '*':
                result *= operand[i+1]
            elif operator[i] == '//':
                result //= operand[i+1]
            elif operator[i] == '**':
                result **= operand[i+1]
            else:
                raise ValueError("Invalid operator type.")
        return result
    except Exception as e:
        raise e
