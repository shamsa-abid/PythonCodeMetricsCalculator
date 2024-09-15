def by_length(arr):
    digit_to_name = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    return [digit_to_name[i] for i in sorted((x for x in arr if 1 <= x <= 9), reverse=True)]
