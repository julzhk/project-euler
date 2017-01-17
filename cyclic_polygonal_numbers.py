#!/usr/bin/env python3
#
# https://projecteuler.net/problem=61
#
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
# all figurate (polygonal) numbers and are generated by the following formulae:
#
# Triangle          P(3,n) = n(n + 1)/2           1, 3, 6, 10, 15, ...
# Square            P(4,n) = n^2                  1, 4, 9, 16, 25, ...
# Pentagonal        P(5,n) = n(3n − 1)/2          1, 5, 12, 22, 35, ...
# Hexagonal         P(6,n) = n(2n − 1)            1, 6, 15, 28, 45, ...
# Heptagonal        P(7,n) = n(5n − 3)/2          1, 7, 18, 34, 55, ...
# Octagonal         P(8,n) = n(3n − 2)            1, 8, 21, 40, 65, ...
#
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
# interesting properties.
#
#    1. The set is cyclic, in that the last two digits of each number is the
#    first two digits of the next number (including the last number with the
#    first).
#    2. Each polygonal type: triangle (P(3,127) = 8128), square
#    (P(4,91) = 8281), and pentagonal (P(5,44) = 2882), is represented by a
#    different number in the set.
#    3. This is the only set of 4-digit numbers with this property.
#
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which
# each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
# octagonal, is represented by a different number in the set.

from itertools import combinations

from utils import (
    is_d_cyclic_set,
    is_polygonal_number,
    is_polygonal_representative_set,
)

if __name__ == '__main__':
    print(
        'Searching for a 2-cyclic set of six 4-digit integers which is '
        '{3,4,5,6,7,8}-polygonal representative ...'
    )
    print(
        'This could take a while as there are 943,566,389766 (approx. 9.43 '
        'billion) 4-digit integer sets which have at least one '
        'polygonal representative in {3,4,5,6,7,8}'
    )
    d = 2
    poly_reps = set(range(3, 9))
    candidates = (m for m in range(10**3, 10**4) if any(is_polygonal_number(m, n) for n in poly_reps))
    result_set = None
    for i, int_set in enumerate(combinations(candidates, 6)):
        print('#{}. Checking if {} is {}-cyclic and has {} polygonal representatives: '.format(i, int_set, d, poly_reps), end='')
        is_d_cyclic = is_d_cyclic_set(int_set, 2)
        has_poly_reps = is_polygonal_representative_set(int_set, poly_reps)
        if is_d_cyclic and has_poly_reps:
            result_set = int_set
            print('YES')
            break
        else:
            print('NO: {}-cyclic={}, is {}-polygonal representative={}'.format(d, is_d_cyclic, poly_reps, has_poly_reps))

    print(
        'The set {} is {}-cyclic and {}-polygonal representative, and it has the sum {}'
        .format(result_set, d, poly_reps, sum(result_set))
    )








