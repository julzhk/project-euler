#!/usr/bin/env python3
#
# https://projecteuler.net/problem=14
#
# The following iterative sequence is defined for the set of positive integers:
#
#   n → n/2 (n is even) n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

import sys

def collatz(n):
    return int(n / 2) if n % 2 == 0 else 3*n + 1

def collatz_sequence_term(seed, k):
    if k == 1:
        return seed
    a = seed
    for i in range(k - 1):
        a = collatz(a)
        if a == 1:
            return None if k > i + 2 else a
    return a

def collatz_sequence(seed):
    n = seed
    yield n
    while True:
        n = collatz(n)
        yield n
        if n == 1:
            break

def longest_sequence_seed(ubound):
    max_seq_seed = 1
    max_seq_len = 1
    for seed in range(1, ubound):
        seq_len = sum(1 for t in collatz_sequence(seed))
        if seq_len > max_seq_len:
            max_seq_len = seq_len
            max_seq_seed = seed
    return max_seq_seed, max_seq_len

if __name__ == '__main__':
    ubound = int(sys.argv[1].strip())
    max_seq_seed, max_seq_len = longest_sequence_seed(ubound)
    print('\nLongest Collatz sequence stats for a seed < {}: seed = {}, length = {}.\n'.format(ubound, max_seq_seed, max_seq_len))

