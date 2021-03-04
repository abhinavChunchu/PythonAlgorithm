class Sort:

    def __init__(self):
        pass


def search_(j, x, search):
    return x[j] == search


def sort_start(search, x):
    leng = len(x)
    center_index = (leng - 1) / 2
    if x[center_index] > search:
        return method_name(0, center_index, search, x)
    return method_name(center_index, leng, search, x)


def method_name(start, center_index, search, x):
    is_present = False
    for i in range(start, center_index):
        result = search_(i, x, search)
        if result:
            is_present = result
            break
    return is_present
