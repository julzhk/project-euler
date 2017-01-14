#!/usr/bin/env python3
#
# https://projecteuler.net/problem=35
#
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?

import sys

from utils import (
    is_prime,
    rotations,
)

def is_circular_prime(n):
    if any(not is_prime(rot) for rot in rotations(n)):
        return False
    return True

def circular_primes(ubound):
    for n in range(1, ubound):
        if is_circular_prime(n):
            yield n

if __name__ =='__main__':
    ubound = int(sys.argv[1].strip())
    count = sum(1 for n in circular_primes(ubound))
    print('\nNo. of circular primes < {}: {}\n'.format(ubound, count))






