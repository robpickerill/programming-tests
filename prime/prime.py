#!/usr/bin/env python


# Get the next prime number!
# You will get a number n (n>=0) and your task is to find the next prime number.

import math
import sys
import argparse


def isPrime(num):

    if num < 2:
        return False

    # Every composite number has a proper factor less than or equal to its square root.
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def main(args):

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=34, type=int)
    args = parser.parse_args()

    prime = False

    while prime is False:
        args.number += 1
        prime = isPrime(args.number)

    print("Next Prime Number: {}").format(args.number)


def test_isPrime():
    assert isPrime(2) is True
    assert isPrime(1) is False
    assert isPrime(12434434249) is True


if __name__ == "__main__":

    main(sys.argv[:1])
