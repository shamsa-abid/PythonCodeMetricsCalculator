def smallest_change(arr):
    ans = sum(1 for i in range(len(arr) // 2)
              if arr[i] != arr[len(arr) - i - 1])
    return ans
