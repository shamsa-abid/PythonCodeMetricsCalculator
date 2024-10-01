def sorted_list_sum(lst):
    def custom_sort(word):
        return (len(word), word)

    return sorted([word for word in lst if len(word) % 2 == 0], key=custom_sort)
