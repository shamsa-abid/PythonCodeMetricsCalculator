def incr_list(l):
    if isinstance(l, list) and all(isinstance(i, int) for i in l):
        try:
            return list(map(lambda x: x + 1, l))
        except Exception as e:
            print(f"Failed to increment list due to: {e}")
        return []
    else:
        return "Input should be a list of integers"
