def by_length(arr):
    dict_numbers = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    return [dict_numbers[i] for i in sorted(filter(lambda x: 1 <= x <= 9, arr), reverse=True)]
