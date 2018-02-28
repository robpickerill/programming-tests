#!/usr/bin/env python

# The most common programming test: fizz buzz test
# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the 
# number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and 
# five print "FizzBuzz".

import argparse, sys

def main(args):
  parser = argparse.ArgumentParser()
  parser.add_argument('-b', '--buzz', default=5, type=int) 
  parser.add_argument('-f', '--fizz', default=3, type=int)
  parser.add_argument('-t', '--total', default=100, type=int)
  args = parser.parse_args()

  for i in range(1,args.total):
    if (i % args.buzz == 0 and i % args.fizz == 0):
      print "FIZZBUZZ: {}".format(i)
      pass
    elif (i % args.buzz == 0):
      print "BUZZ: {}".format(i)
      pass
    elif (i % args.fizz == 0):
      print "FIZZ: {}".format(i)
      pass
    else:
      print "PASS: {}".format(i)
  
if __name__ == "__main__":
  main(sys.argv[1:])
