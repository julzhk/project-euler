#!/usr/bin/env python3
#
# https://projecteuler.net/problem=153

import math

from utils import (
    complexify,
    complex_divide,
    complex_format,
    complex_reflections,
    integerise,
)


def is_gaussian_integer(z):
    """
        Checks whether a given real or complex number is a Gaussian integer,
        i.e. a complex number g = a + bi such that a and b are integers.
    """
    if type(z) == int:
        return True
    return z.real.is_integer() and z.imag.is_integer()


def gaussian_divisors(g):
    """
        Generates a sequence of Gaussian divisors of a rational or Gaussian
        integer g, i.e. a Gaussian integer d such that g / d is also a Gaussian
        integer.
    """
    if not is_gaussian_integer(g):
        return
    g = complex_format(g)
    ubound = math.ceil(math.sqrt(abs(g))) if g.real and g.imag else int(g.real) if g.real else int(g.imag)
    for a in range(ubound + 1):
        for b in range(ubound + 1):
            if a or b:
                d = complex(a, b)
                if is_gaussian_integer(complex_divide(g, d)):
                    for f in complex_reflections(d):
                        yield f


def s(g):
    """
        Returns the sum of the Gaussian divisors of a Gaussian integer where
        the divisors have positive real parts.
    """
    return sum(int(g.real) for g in gaussian_divisors(g) if g.real > 0)


def sum_s(n):
    """
        Returns the sum of the sums of Gaussian divisors of integers 1..n, e.g.

            sum_s(5) = s(1) + s(2) + s(3) + s(4) + s(5)

    """
    return sum(s(k) for k in range(1, n + 1))
