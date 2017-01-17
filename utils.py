import math

from itertools import (
    permutations,
    starmap,
)
from functools import partial

def digits(n, reverse=False):
    """
        Generates the sequence of digits of a given integer n, starting from
        the most significant digit, by default. If reverse is True then the
        sequence is generated from the least significant digit, e.g.

            123 -> 1, 2, 3      (with no reverse or reverse=False)
            123 -> 3, 2, 1      (with reverse=True)
    """
    s = str(n) if not reverse else str(n)[::-1]
    for c in s:
        yield int(c)


def int_from_digits(digits):
    """
        Returns a positive integer n which is a decimal expansion of a
        sequence of digits in descending order from the most significant
        digit. The input can be a sequence (list, tuple) or a generator,
        e.g.

            [1,2,3] -> 1x10^2 + 2x10^1 + 3x10^0 = 123
            (2, 4, 5, 1) -> 2x10^3 + 4x10^2 + 5x10 + 1x10^0 = 2451
    """
    dgs = list(digits)
    n = len(dgs)
    return sum(d*10**i for d, i in zip(dgs, reversed(range(n))))


def rotations(n):
    """
        Generates a sequence of (right) rotations of a positive integer n, e.g.

            1234 -> 4123, 3412, 2341, 1234
    """
    digs = list(digits(n, reverse=True))
    n = len(digs)
    for i in range(n):
        yield sum(digs[(j + i) % n] * 10**j for j in range(n))


def int_permutations(n):
    """
        Generates a sequence of permutations of a given positive integer n in
        lexicographic order, e.g.

            123 -> 123, 132, 213, 231, 312, 321
    """
    for p in permutations(digits(n)):
        yield int_from_digits(p)


def concatenate(int_seq):
    """
        Produces an integer which is a "concatenation" of the digits of a
        sequence of positive integers, e.g.

            [12, 345, 6789] -> 123456789
    """
    return int(''.join([str(n) for n in int_seq]))


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


def primes(index_range=None, int_range=None):
    """
        Generates all primes, by default. Can also generate primes within a
        given index range (e.g. the first 50 primes, or the 20th to the 50th
        primes) by using the 'index_range' option, or a given interval for
        the primes (e.g. primes between 100 and 1000) by using the
        'int_range' option.
    """    
    if index_range:
        n = 2
        i = 1
        while i not in index_range:
            if is_prime(n):
                i += 1
            n += 1
        while i in index_range:
            if is_prime(n):
                yield n
                i += 1
            n += 1
        return
    elif int_range:
        for n in int_range:
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


def polygonal_number(n, k):
    """
        Returns the kth n-gonal number P(n, k) given by the following formula:

            P(n, k) = [(n - 2)k^2 - (k - 4)n] / 2
    """
    return int(((n - 2)*k**2 - (n - 4)*k) / (2))


def n_polygonal_number_func(n):
    """
        Returns a function to generate the n-gonal numbers for a given n - 
        mathematically this function is obtained by restricting the general
        function, which is a function of two variables n and k, to the given
        value of n, e.g. to have a triangular number generating function do
        the following

            >>> tri = n_polygonal_number_func(3)

            >>> tri
            >>> functools.partial(<function polygonal_number at 0x10f53bea0>, n=3)
            
            >>> [tri(k=i) for i in range(1, 11)]

            >>> [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """

    return partial(polygonal_number, n=n)


def is_polygonal_number(m, n):
    """
        Checks whether a given number m is a polygonal number for some n, i.e.
        whether it is an n-gonal number for some n > 2.
    """
    if m == 1:
        return True
    k = (((n - 4) + math.sqrt((n - 4)**2 + 8*m*(n - 2))) / (2*(n - 2)))
    return int(k) if k.is_integer() else False


def is_polygonal_representative_set(int_set, poly_reps):
    """
        Checks whether a given set of positive integers contains polygonal
        numbers of every type (n) specified in the set (or sequence)
        'poly_reps', e.g. whether for every value of n in 'poly_reps' there
        is an n-gonal number in the given set of integers, e.g. the set
        {2882, 8128, 8281} contains a triangular number (8128), a square number
        (8281) and a pentagonal number (8128).
    """
    return any(
        (
            False not in starmap(is_polygonal_number, zip(int_set, poly_rep_perm))
            for poly_rep_perm in permutations(poly_reps)
        )
    )


def is_d_cyclic_set(int_seq, d):
    """
        Checks whether a given set (or sequence) of positive integers has the
        d-cyclic property, namely that there exists an (ordered) sequence of
        all the integers from this set such that for any two consecutive
        integers in the sequence the d least significant digits of the first
        integer are equal to the d most significant digits of the second,
        this being true for the last and first integers as well, e.g. the
        set {2882, 8128, 8281} is 2-cyclic because the sequence

            8128, 2882, 8281

        has the 2-cyclic property.
    """
    m = len(int_seq)
    for p in permutations(int_seq):
        if all(str(p[i])[-d:] == str(p[(i+1) % m])[:d] for i in range(m)):
            return True
    return False


def integerise(f):
    """
        Turns a float into an integer if it is an integer, otherwise returns
        the same float.
    """
    return int(f) if f.is_integer() else f


def complexify(r):
    """
        Turns a real number into a complex number if it not complex, otherwise
        returns the same number.
    """
    return complex(r) if not type(r) == complex else r


def complex_format(z):
    """
        Formats a complex number z = a + bi to ensure that real and/or
        imaginary parts a and b are displayed as integers if they are actually
        integers. This is because the display of Python native complex numbers
        is a bit inconsistent: complex numbers with a 0 real part can sometimes
        be displayed with the real part as -0. Also, complex numbers such as
        1 - 2.0j are better read as 1 - 2j.
    """
    if type(z) == int:
        return complex(z)
    elif type(z) == float:
            return complex(integerise(z))
    elif type(z) == complex:
        a, b = map(integerise, [z.real, z.imag])
        return complex(a, b)


def complex_reflections(z):
    """
        Generates a sequence of reflections of a complex number z = a + bi in the real
        and imaginary planes:

            z = a + bi -> a + bi, a - bi, -a - bi, -a + bi
    """
    z = complex_format(z)
    a, b = map(integerise, [z.real, z.imag])
    if a and b:
        yield z.conjugate()
        yield -z
        yield -z.conjugate()
        yield z
    elif a and not b:
        yield -a
        yield a
    elif b and not a:
        yield complex(0, b).conjugate()
        yield complex(0, b)
        

def complex_divide(z1, z2):
    """
        Divides complex numbers using explicit formulae for the real and
        imaginary parts of the quotient. Python supports division of native
        complex numbers but this is reported to be inconsistent for large
        operands.
    """
    a, b, c, d = z1.real, z1.imag, z2.real, z2.imag
    m = c**2 + d**2
    u, v = map(integerise, [(a*c + b*d) / m, (b*c - a*d) / m])
    return complex(u, v)
