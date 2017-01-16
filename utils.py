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


def primes(up_to_index=None, index_range=None, within=None, below=None):
    """
        Generates all primes. Four mutually exclusive options exist:
        'up_to_index' indicates the number of consecutive primes to generate,
        starting from 2; 'index_range' indicates the range of indices for the
        primes to be generated, e.g. the 50th to 100th primes; 'within'
        indicates the range of positive integers within which the primes should
        be generated; 'below' indicates a strict upper bound for the generated
        primes.
    """    
    if up_to_index or index_range or within or below:
        if up_to_index:
            n = 2
            i = 1
            while i <= up_to_index:
                if is_prime(n):
                    yield n
                    i += 1
                n += 1
        elif index_range:
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
        yield z
        yield z.conjugate()
        yield -z
        yield -z.conjugate()
    elif a and not b:
        yield a
        yield -a
    elif b and not a:
        yield complex(0, b)
        yield complex(0, b).conjugate()


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
