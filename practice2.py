import numpy as np



def lev(str_x, str_y):
    len_x = len(str_x) + 1
    len_y = len(str_y) + 1
    m = np.zeros((len_x, len_y))


    # Initial cost data
    for x in range(len_x):
        m[x, 0] = x
    for y in range(len_y):
        m[0, y] = y

    for x in range(1, len_x):
        for y in range(1, len_y):
            if str_x[x - 1] == str_y[y - 1]:
                cost = 0
            else:
                cost = 1
            m[x, y] = min(
                m[x - 1, y] + 1,
                m[x - 1, y - 1] + cost,
                m[x, y - 1] + 1)
    # print(m)
    return m[len_x - 1, len_y - 1]


def normalize(s):
    normalized = s.upper().replace(",", "").replace(";", "").replace(".", "")
    tokens = normalized.split(" ")
    tokens.sort()
    normalized = " ".join(tokens)
    return normalized


def get_lowest_scored_for_list(s, s_list, threshold=2):
    s_normal = normalize(s)
    s_list_normal = []

    for elem in s_list:
        s_list_normal.append(normalize(elem))

    lowest = threshold, ""  # Cost, index
    for i, elem in enumerate(s_list_normal):
        cost = lev(s_normal, elem)
        if cost <= lowest[0]:
            lowest = cost, s_list[i]

    return lowest[1]


assert 1 == lev('Food', "Fool")
assert 0 == lev('hi', 'hi')
assert get_lowest_scored_for_list("food", ["Cheese", "fool", "food"]) == "food"
assert get_lowest_scored_for_list("food", ["Cheese", "fool", "pizza"], 3) == "fool"
assert get_lowest_scored_for_list("John Lockwood", ["Lockwood, Johb", "Jack Lookout", "Jeff Roberts", "John Locoweed"]) == "Lockwood, Johb"
assert get_lowest_scored_for_list("John Lockwood", ["Lockwood, Johb", "Jack Lookout", "Jeff Roberts", "John Locoweed"], 1) == "Lockwood, Johb"
assert get_lowest_scored_for_list("John Lockwood", ["Lockwood, Johb", "Jack Lookout", "Jeff Roberts", "John Locoweed"], 0) == ""

