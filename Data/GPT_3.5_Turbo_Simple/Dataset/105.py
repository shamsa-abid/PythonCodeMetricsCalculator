def by_length(arr):
    number_names = {1: "One", 2: "Two", 3: "Three", 4: "Four",
                    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]

    result = [number_names[num] for num in reversed_arr]

    return result
