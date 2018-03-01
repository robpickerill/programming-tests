#!/usr/bin/env python

import sys
import argparse


def test_long():

    assert countlong("hi marcel") == 0
    assert countlong("I am going to trek Machu Picchu") == 3
    assert countlong("PYTEST TESTS PYTHON") == 17


def test_short():

    assert countlong("hi marcel") == 0
    assert countlong("I am going to trek Machu Picchu") == 3
    assert countlong("PYTEST TESTS PYTHON") == 17


def countlong(string):

    count = 0

    for char in string:
        if char.isupper():
            count += 1

    return count


def countshort(string):

    count = sum(char.isupper() for char in string)
    return count


def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--string', default="ACamelCaseString", type=str)
    args = parser.parse_args()

    print("LONG - Number of Capital Letters: {}").format(countlong(args.string))
    print("SHORT - Number of Capital Letters: {}").format(countshort(args.string))


if __name__ == "__main__":

    main(sys.argv[1:])
