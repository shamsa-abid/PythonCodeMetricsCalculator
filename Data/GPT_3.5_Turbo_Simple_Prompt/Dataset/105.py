def by_length(arr):
    nums = {1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    # Filter and sort integers between 1 and 9 inclusive
    filtered_nums = [num for num in arr if 1 <= num <= 9]
    filtered_nums.sort()

    # Reverse the filtered array and replace digits with corresponding names
    result = [nums[num] for num in filtered_nums[::-1]]

    return result


# Test cases
# ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']
