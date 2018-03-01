#!/usr/bin/env python

# I have a cat and a dog.
# I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now.
#
# NOTES:
#
# humanYears >= 1
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that


def catYears(humanYears):
    return 15 if humanYears == 1 else 4 * humanYears + 16


def dogYears(humanYears):
    return 15 if humanYears == 1 else 5 * humanYears + 14


def test_catYears():
    assert catYears(1) == 15
    assert catYears(2) == 24
    assert catYears(3) == 28
    assert catYears(9) == 52


def test_dogYears():
    assert dogYears(1) == 15
    assert dogYears(2) == 24
    assert dogYears(3) == 29
    assert dogYears(9) == 59
