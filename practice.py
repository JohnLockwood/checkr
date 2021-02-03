import numpy as np


def lev (str_x, str_y):
    len_x = len(str_x) + 1
    len_y = len(str_y) + 1
    m = np.zeros((len_x, len_y))

    for x in range(len_x):
        m[x, 0] = x
    for y in range(len_y):
        m[0, y] = y
    # print(m)

    for x in range(1, len_x):
        for y in range(1, len_y):
            if str_x[x - 1] == str_y[y - 1]:
                m[x, y] = min(
                    m[x, y - 1] + 1,
                    m[x - 1, y - 1],
                    m[x -1, y] + 1,
                )
            else:
                m[x, y] = min(
                    m[x, y - 1] + 1,
                    m[x - 1, y - 1] + 1,
                    m[x - 1, y] + 1,
                )
    # print(m)
    return m[len_x - 1, len_y -1]



# assert lev("Food", "Fool") == 1
# assert lev("Fool", "Feel") == 2
#
print(f"lev('food, 'feed') = {lev('food', 'feed')}")
print(f"lev('food, 'fool') = {lev('food', 'fool')}")
print(f"lev('food, 'food') = {lev('food', 'food')}")
print(f"lev('food, 'foodstuff') = {lev('food', 'foodstuff')}")
print(f"lev('foodstuff, 'food') = {lev('foodstuff', 'food')}")