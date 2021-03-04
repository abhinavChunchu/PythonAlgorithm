import pandas
import Sort


class Simple:
    def __init__(self):
        pass

    x = [1, 5, 7, 8, 9, 4, 6]

    search = 3

    # should return the index of search item
    x.sort()
    print(x)
    ind = Sort.sort_start(search, x)

    print('hasElement: {result}'.format(result=ind))

