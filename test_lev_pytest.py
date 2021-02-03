
from lev import *


l_test = ["Jack Lockwood", "Jeff Roberts", "Len Roberts", "Mable Lackwood"]
s_test = "John Lockwood"


def test_known_score():
    assert lev('foot', 'fool') == 1


def test_low_score_returns_lowest_scored():
    matched = find_in_list(s_test, l_test, 3)
    assert matched == "Jack Lockwood"


def test_no_match_if_below_cutoff():
    # Exact match works fine
    matched = find_in_list(s_test, l_test)
    assert matched == ""


def test_exact_match_works_by_default():
    # Exact match works fine
    l_test.append(s_test)
    matched = find_in_list(s_test, l_test)
    assert matched == s_test
    l_test.pop()
    assert s_test not in l_test


def test_normalize_name_removes_punctuation():
    n = normalize_name("Mr. John Jones, Esq.")
    assert "." not in n
    assert "," not in n


def test_normalize_sorts_and_uppercases():
    n = normalize_name("Jenniffer Cajal")
    assert n == "CAJAL JENNIFFER"


def test_normalized_match_works():
    l_test_local = l_test.copy()
    l_test_local.append(s_test)
    normal_me = "Lockwood, John"
    m = find_in_list_with_transposition_support(normal_me, l_test_local)
    assert m == s_test

