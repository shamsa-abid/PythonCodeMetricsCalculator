def by_length(arr):
    dic = {
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
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr, reverse=True)
    new_arr = [dic[num] for num in sorted_arr]
    return new_arr
