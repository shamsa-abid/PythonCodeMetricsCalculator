def move_one_ball(arr):
    if not arr:
        return True

    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    sorted_arr = sorted(arr)

    for i in range(len(arr)):
        if is_sorted(arr):
            return True
        arr.insert(0, arr.pop())

    return is_sorted(arr)
