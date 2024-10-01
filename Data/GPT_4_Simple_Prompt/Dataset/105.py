def by_length(arr):
    numbers = ["Zero", "One", "Two", "Three", "Four",
               "Five", "Six", "Seven", "Eight", "Nine"]
    arr = [numbers[i] for i in arr if i > 0 and i < 10]
    return sorted(arr, reverse=True)
