from itertools import chain


def get_row(lst, x):
    coords = [(i, j) for i, sub_list in enumerate(lst)
              for j, element in enumerate(sub_list) if element == x]
    coords.sort(key=lambda coord: (coord[0], -coord[1]))
    return coords
