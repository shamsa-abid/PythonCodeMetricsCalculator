def sorted_list_sum(lst):
    def filter_strings(lst):
        return [word for word in lst if len(word) % 2 == 0]

    def sort_strings(lst):
        return sorted(lst, key=lambda x: (len(x), x))

    filtered_list = filter_strings(lst)
    sorted_list = sort_strings(filtered_list)

    return sorted_list
