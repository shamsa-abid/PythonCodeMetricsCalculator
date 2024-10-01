def add(lst):
    even_odd_indices = [lst[i]
                        for i in range(len(lst)) if i % 2 != 0 and lst[i] % 2 == 0]
    return sum(even_odd_indices)
