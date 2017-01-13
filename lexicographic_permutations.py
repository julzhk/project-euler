#!/usr/bin/env python3

# https://projecteuler.net/problem=24

# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
# listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
# 6, 7, 8 and 9?

from itertools import permutations

def lexicographic_permutation(charset, perm_index):
	c = 0
	for p in permutations(charset):
		c += 1
		if c == perm_index:
			return p

if __name__ == '__main__':
	print('\nMillionth lexicographic permutation of digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9: {}\n'.format(
		''.join(str(c) for c in lexicographic_permutation(range(10), 10**6)))
	)
