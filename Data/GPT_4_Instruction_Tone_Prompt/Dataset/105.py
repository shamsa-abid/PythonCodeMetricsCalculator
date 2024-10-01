def by_length(arr):
    num_name = {1: "One", 2: "Two", 3: "Three", 4: "Four",
                5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    sorted_arr = sorted([i for i in arr if 1 <= i <= 9], reverse=True)
    return [num_name[i] for i in sorted_arr]
