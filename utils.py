from itertools import permutations

def digits(n, reverse=False):
    """
        Generates the sequence of digits of a given integer n, starting from
        the most significant digit, by default. If reverse is True then the
        sequence is generated from the least significant digit.
    """
    s = str(n) if not reverse else str(n)[::-1]
    for c in s:
        yield int(c)


def int_from_digits(digits):
    """
        Returns a positive integer n which is a decimal expansion
        of an iterable of digits in descending order from the most
        significant digit, e.g.

            [1,2,3] --> 1x10^2 + 2x10^1 + 3x10^0 = 123
    """
    dgs = list(digits)
    n = len(dgs)
    return sum(d*10**i for d, i in zip(dgs, reversed(range(n))))


def rotations(n):
    """
        Generates a sequence of (right) rotations of a given positive integer n.
    """
    digs = list(digits(n, reverse=True))
    n = len(digs)
    for i in range(n):
        yield sum(digs[(j + i) % n] * 10**j for j in range(n))


def int_permutations(n):
    """
        Generates a sequence of permutations of a given positive integer n in
        lexicographic order.
    """
    for p in permutations(digits(n)):
        yield int_from_digits(q)


def concatenate(int_seq):
    """
        Produces an integer which is a "concatenation" of the digits of a
        sequence of positive integers, e.g.

            [12, 345, 6789] -> 123456789
    """
    return int(''.join([str(n) for n in int_seq]))


def product(int_seq):
    """
        Returns the product of a sequence of integers.
    """
    t = 1
    for i in int_seq:
        t *= i
    return t


def factorial(n):
    """
        Iteratively calculates factorial of n.
    """
    if n in [0, 1]:
        return n
    fact = 1
    for k in reversed(range(1, n + 1)):
        fact *= k
    return fact


def is_prime(n):
    """
        Simple but fairly quick primality checker.
    """
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**(1/2) + 1), 2):
        if n % i == 0:
            return False    

    return True


def primes(number=None, within=None, below=None):
    """
        Generates all primes. Three mutually exclusive options exist: 'number'
        indicates the number of consecutive primes to generate, starting from 2;
        'within' indicates the range of positive integers within which the
        primes should be generated; 'below' indicates a strict upper bound for
        the generated primes.
    """    
    if number or within or below:
        if number:
            n = 2
            i = 1
            while i <= number:
                if is_prime(n):
                    yield n
                    i += 1
                n += 1
        elif within:
            for n in within:
                if is_prime(n):
                    yield n
        else:
            for n in range(1, below):
                if is_prime(n):
                    yield n
        return

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def fibonacci():
    """
        Generates the Fibonacci sequence defined by

            f(1) = 1, f(2) = 1, f(n) = f(n - 1) + f(n - 2) for n > 2

        The first 10 terms are

            1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    """
    a = b = 1
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a + b



