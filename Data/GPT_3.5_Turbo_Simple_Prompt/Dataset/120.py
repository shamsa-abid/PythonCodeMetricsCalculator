def maximum(arr, k):
    arr.sort()
    return arr[-k:]


# Example usage
arr1 = [-3, -4, 5]
k1 = 3
print(maximum(arr1, k1))  # Output: [-4, -3, 5]

arr2 = [4, -4, 4]
k2 = 2
print(maximum(arr2, k2))  # Output: [4, 4]

arr3 = [-3, 2, 1, 2, -1, -2, 1]
k3 = 1
print(maximum(arr3, k3))  # Output: [2]
