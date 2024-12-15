def is_nested(string):
    opening_brackets = []
    closing_brackets = []

    for i in range(len(string)):
        if string[i] == '[':
            opening_brackets.append(i)
        else:
            closing_brackets.append(i)

    closing_brackets.reverse()
    count = 0
    i = 0
    l = len(closing_brackets)

    for idx in opening_brackets:
        if i < l and idx < closing_brackets[i]:
            count += 1
            i += 1

    return count >= 2
