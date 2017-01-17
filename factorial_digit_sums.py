#!/usr/bin/env python3
#
# https://projecteuler.net/problem=20
#
# The factorial function f(n) is defined for non-negative integers:
# it is the product of the first n consecutive integers 1, 2, ... , n 
# when n is positive, and 1 when n is 0. e.g. 4! = 4 x 3 x 2 x 1 = 24
# and 0! = 1 by definition.
#
# The factorial digit sum of n is the sum of the digits of n!.

import sys

from math import factorial

from utils import digits

def digit_sum(n):
    if n < 0:
        return digit_sum(-n)
    elif n in range(0, 10):
        return n
    return sum(d for d in digits(n))

def factorial_digit_sum(n):
    return digit_sum(factorial(n))

if __name__ == '__main__':
    n = int(sys.argv[1].strip())
    fact = factorial(n)
    digs = digits(fact)
    digit_sum_str = ' + '.join(str(d) for d in digs)
    fact_digit_sum = digit_sum(n)
    print('\n{}! = {}, digit sum = {} = {}\n'.format(n, fact, digit_sum_str, fact_digit_sum))
