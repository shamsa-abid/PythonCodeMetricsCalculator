def move_one_ball(arr):
    if len(arr) == 0:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return arr[0] >= arr[-1]
    return True
