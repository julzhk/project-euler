#!/usr/bin/env python3

# https://projecteuler.net/problem=20

import sys

def digits(n):
    m = n
    while m:
        d = m % 10
        yield d
        m //= 10

def digit_sum(n):
    if n < 0:
        return digit_sum(-n)
    elif n in range(0, 10):
        return n
    return sum(d for d in digits(n))

def factorial(n):
    if n in [0, 1]:
        return n
    fact = 1
    for k in reversed(range(1, n + 1)):
        fact *= k
    return fact

def factorial_digit_sum(n):
    return digit_sum(factorial(n))

if __name__ == '__main__':
    n = int(sys.argv[1].strip())
    fact = factorial(n)
    digs = digits(fact)
    digit_sum_str = ' + '.join(str(d) for d in digs)[::-1]
    fact_digit_sum = digit_sum(n)
    print('\n{}! = {}, digit sum = {} = {}\n'.format(n, fact, digit_sum_str, fact_digit_sum))
