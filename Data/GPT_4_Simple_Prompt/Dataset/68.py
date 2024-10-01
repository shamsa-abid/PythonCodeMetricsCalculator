def pluck(arr):
    even_nums = [(num, idx) for idx, num in enumerate(arr) if num % 2 == 0]

    if even_nums:
        # Defaults to sorting by first element, then second etc.
        even_nums.sort()
        return list(even_nums[0])
    else:
        return []
