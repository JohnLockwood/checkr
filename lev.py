import numpy as np
from typing import List


def lev(str1, str2):

    """ Levenstein match return 0 on exact match, one on one change, etc.  Note that some implementations
        allow insert/update/delete to be scored separately.  Non-recursive implementations are least expensive
        because you're only scanning both strings once.
    """
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


def find_in_list(needle: str, haystack: List[str], cutoff: int = 2) -> str:
    """Returns the last match with the lowest Levenshtein score (closest match) that is at or below the cutoff value
       If no match return an empty string.

       An improvement could consider ties and return a list.

       Could also do other preprocessing such as case-insensitive compare (run upper on everything up front). "
    """

    assert haystack is not None
    assert None not in haystack
    assert str is not None

    lowest = cutoff
    match = ''
    for i, elem in enumerate(haystack):
        score = lev(needle, elem)

        if score <= lowest:
            lowest = score
            match = elem

    return match


def remove_punctuation(source: str) -> str:
    assert str is not None
    return source.replace(",", "").replace(".", "").replace(";", "")


def normalize_name(source: str) -> str:
    """transforms a name into a sorted list of uppercase tokens, with punctuation removed"""
    name = remove_punctuation(source).upper()
    tokens = name.split(" ")
    tokens.sort()
    return " ".join(tokens)


def find_in_list_with_transposition_support(needle: str, haystack: List[str], cutoff: int = 2) -> str:
    names = []
    for name in haystack:
        names.append(normalize_name(name))
    return find_in_list(normalize_name(needle), names, cutoff)



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

