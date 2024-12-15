def incr_list(l: list):
    try:
        return list(map(lambda x: x+1, l))
    except TypeError as e:
        print(f"Input should be a list of integers. Error: {str(e)}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return []
