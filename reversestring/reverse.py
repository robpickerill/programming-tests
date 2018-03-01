#!/usr/bin/env python

# Complete the solution so that it reverses the string value passed into it.


def reverse(string):
    return string[::-1]


def test_reverse():
    assert reverse("theworldisflat") == "talfsidlroweht"
