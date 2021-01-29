import numpy as np
from typing import List


def lev(str1, str2):
    x_len = len(str1) + 1
    y_len = len(str2) + 1
    matrix = np.zeros((x_len, y_len))

    for x in range(x_len):
        matrix[x, 0] = x
    for y in range(y_len):
        matrix[0, y] = y

    for x in range(1, x_len):
        for y in range(1, y_len):
            if str1[x-1] == str2[y-1]:
                matrix[x, y] = min(
                    matrix[x, y - 1] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x - 1, y] + 1
                ) 
            else:
                matrix[x, y] = min(
                    matrix[x, y - 1] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x - 1, y] + 1
                ) 

    # print(matrix)
    return matrix[x_len - 1, y_len - 1]


def find_in_list(needle: str, haystack: List[str], use_numpy: bool = True) -> str:
    """Returns the first match with the lowest Levenshtein score (closest match)

       An improvement could consider ties.
    """

    assert haystack is not None
    assert None not in haystack
    assert str is not None

    unset_high_score = 1000
    lowest = unset_high_score
    match = ''
    for elem in haystack:
        if use_numpy:
            score = lev(needle, elem)
        else:
            score = lev_no_numpy(needle, elem)

        if score < lowest:
            lowest = score
            match = elem

    return match


def lev_no_numpy(str1, str2):
    x_len = len(str1) + 1
    y_len = len(str2) + 1
    matrix = [[0 for y in range(y_len)] for x in range(x_len)]
    # matrix = np.zeros((x_len, y_len))

    for x in range(x_len):
        matrix[x][0] = x
    for y in range(y_len):
        matrix[0][y] = y

    for x in range(1, x_len):
        for y in range(1, y_len):
            if str1[x-1] == str2[y-1]:
                matrix[x][y] = min(
                    matrix[x][y - 1] + 1,
                    matrix[x - 1][y - 1],
                    matrix[x - 1][y] + 1
                )
            else:
                matrix[x][y] = min(
                    matrix[x][y - 1] + 1,
                    matrix[x - 1][y - 1] + 1,
                    matrix[x - 1][y] + 1
                )

    # print(matrix)
    return matrix[x_len - 1] [y_len - 1]

