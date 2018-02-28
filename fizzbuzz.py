#!/usr/bin/env python

# The most common programming test: fizz buzz test
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the
# number and for the multiples of five print "Buzz".
# For numb`ers which are multiples of both three and
# five print "FizzBuzz"

# This is overkill, but the aim here is to include
# unit tests automated by Travis-CI.


import sys

import argparse


def fizzbuzz(number, fizz, buzz):

    try:
        if (number % fizz == 0 and number % buzz == 0):
            return "FIZZBUZZ"
        elif (number % fizz == 0):
            return "BUZZ"
        elif (number % buzz == 0):
            return "FIZZ"
        else:
            return
    except TypeError:
        return None


def main(args):

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fizz', default=3, type=int)
    parser.add_argument('-b', '--buzz', default=5, type=int)
    parser.add_argument('-t', '--total', default=100, type=int)
    args = parser.parse_args()

    for i in range(1, args.total):
        result = fizzbuzz(i, args.fizz, args.buzz)
        if result:
            print "{} - {}".format(i, result)


def test_fizzbuzz():

    assert fizzbuzz(15, 3, 5) == "FIZZBUZZ"
    assert fizzbuzz(4, 2, 5) == "BUZZ"
    assert fizzbuzz("dave", 3, 5) is None, "input was a string, should return value: None"


if __name__ == "__main__":

    main(sys.argv[1:])
