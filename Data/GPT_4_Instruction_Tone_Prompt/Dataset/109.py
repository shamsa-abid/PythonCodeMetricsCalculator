def move_one_ball(arr):
    arr = arr[::-1]
    for i in range(len(arr)):
        if sorted(arr[i:]+arr[:i]) == arr[i:]+arr[:i]:
            return True
    return False
