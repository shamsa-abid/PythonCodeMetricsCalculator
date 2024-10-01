def move_one_ball(arr):
    if len(arr) == 0:
        return True

    arr_orig = arr.copy()
    arr.sort()

    for i in range(len(arr)):
        if arr_orig == arr:
            return True
        arr_orig = [arr_orig[-1]] + arr_orig[:-1]

    return False
