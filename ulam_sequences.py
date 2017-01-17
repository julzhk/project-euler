#!/usr/bin/env python3
#
# https://projecteuler.net/problem=167

import sys

from collections import Counter

def ulam(a, b, k):
    """
    An integer sequence defined as follows:
 
        U(a, b, 1) = a
        U(a, b, 2) = b
        U(a, b, k: k > 2) = min{U(a,b,k-i)+U(a,b,k-j) for i, j < k such that i != j and sum is unique}
 
        e.g. first 25 terms of the U(2, 5) sequence:
 
            2, 5, 7, 9, 11, 12, 13, 15, 19, 23, 27, 29, 35, 37, 41, 43, 45, 49, 51, 55, 61, 67, 69, 71, 79 ...
    """
    if k == 1:
        return a
    elif k == 2:
        return b

    terms = {1: a, 2: b}
    min_bound = ulam(a, b, k - 1)
    terms[k - 1] = min_bound
    sums = Counter()

    for i in range(1, k - 1):
        for j in range(i + 1, k):
            try:
                ti = terms[i]
            except KeyError:
                ti = ulam(a, b, i)
                terms[i] = ti
            else:
                try:
                    tj = terms[j]
                except KeyError:
                    tj = ulam(a, b, j)
                    terms[j] = tj

            s = ti + tj
            if s > min_bound:
                sums[s] += 1

    return min(s for s in sums if sums[s] == 1 and s > min_bound)


def ulam_sequence(a, b, num_terms):
    for k in range(1, num_terms + 1):
        yield ulam(a, b, k)

if __name__ == '__main__':
    a, b, nt = map(int, sys.argv[1:4])
    print()
    for u in ulam_sequence(a, b, nt):
        print('{}'.format(u), end=' ')
    print('\n')



