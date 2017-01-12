#!/usr/bin/env python3

# https://projecteuler.net/problem=168

import sys

def right_rotation(n):
    s = str(n)
    return int(''.join([c for c in s[-1] + s[:-1]]))

def is_right_rotator(n):
    """
    An integer n is called a right rotator if it is a divisor
    of its right-rotation, e.g. 142857 divides its right rotation
    714285.    
    """
    return (right_rotation(n) % n == 0)

def right_rotators(int_range=range(11, 10**6)):
    for n in int_range:
        if is_right_rotator(n):
            yield n


if __name__ == "__main__":
    m = int(sys.argv[1].strip())
    ans = int(str(sum(n for n in right_rotators(int_range=range(11, 10**m))))[-5:])
    print('\nLast 5 digits of the sum of all right rotators in the range 10 < n < 10^{}: {}\n'.format(m, ans))
