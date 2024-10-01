def odd_count(lst):
    output = []
    for i, number_str in enumerate(lst):
        odd_count = sum(map(lambda x: int(x) & 1, number_str))
        result = 'the number of odd elements in the string of the input.'\
            .replace('in ', str(odd_count)+'n ')\
            .replace('string ', 'str'+str(odd_count)+'ng ')\
            .replace(' of the input.', ' of the '+str(odd_count)+'nput.')
        output.append(result)
    return output
