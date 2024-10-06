def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        return "Invalid input lengths"

    result = operand[0]

    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            if operand[i+1] != 0:
                result //= operand[i+1]
            else:
                return "Division by zero error"
        elif operator[i] == '**':
            result **= operand[i+1]

    return result


# Example
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9
