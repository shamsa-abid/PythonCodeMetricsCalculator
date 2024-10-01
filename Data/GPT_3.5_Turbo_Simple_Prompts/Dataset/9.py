
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    for i in range(len(numbers)):
        max_num = max(numbers[:i+1])
        rolling_max_list.append(max_num)
    return rolling_max_list
