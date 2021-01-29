
from lev import lev, find_in_list


def test_one_change():
    assert lev('foot', 'fool') == 1


def test_low_score_returns_lowest_scored():
    s_test = "John Lockwood"
    l_test = ["Jack Lockwood", "Jeff Roberts", "Len Roberts", "Mable Lackwood"]
    matched = find_in_list(s_test, l_test, False)
    assert matched == "Jack Lockwood"

    # Now try with exact match
    l_test.append(s_test)
    matched = find_in_list(s_test, l_test, False)
    assert matched == s_test

