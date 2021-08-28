"""
Given two strings, s and t, return the length of their longest subsequence.

Ex: Given the following strings s and t

s = "xyz", t = "xyz". return 3.
Ex: Given the following strings s and t

s = "abca", t = "acea", return 3.
Ex: Given the following strings s and t

s = "abc", t = "def", return 0.
"""


from typing import List


def lsp(pattern: str) -> List[int]:
    """
    KMP Algorithm

    defines the longest suffix prefix for the pattern.
    eg "dsgwadsgz" = [0, 0, 0, 0, 0, 1, 2, 3, 0]
    """

    i, j = 1, 0
    lsp = [0] * len(pattern)

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lsp[i] = j
            i += 1

        else:
            if j > 0:
                j = lsp[j - 1]
            else:
                i += 1
    return lsp


def str_str(haystack: str, needle: str) -> int:
    """
    returns the first index of the needle in the haystack
    """
    i, j = 0, 0
    n, m = len(haystack), len(needle)

    lsp_result = lsp(needle)

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        else:
            if j > 0:
                j = lsp_result[j - 1]
            else:
                i += 1

        if j == m:
            return i - m

    return -1


if __name__ == "__main__":
    assert lsp("dsgwadsgz") == [0, 0, 0, 0, 0, 1, 2, 3, 0]
    assert str_str("dsgwadsgydsgwadsgydsgwadsgbdsgwadsgz", "dsgwadsgz") == 27

#       i     j
# a a a c a a a a a c
# 0 1 2 0 1 2 3 3 3 4
