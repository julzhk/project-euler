def digits(n, pos=False):
    """
        Generates the sequence of digits of a given integer n,
        starting from the least significant digit. If pos is
        True then it returns a sequence of digits and their
        relative positions in the decimal expansion of n.
    """
    m = n
    if pos:
        i = 0
    while m:
        d = m % 10
        if pos:
            yield d, i
            i += 1
        else:
            yield d
        m //= 10


def int_from_digits(digits):
    """
        Returns a positive integer n which is a decimal expansion
        of an iterable of digits in descending order from the most
        significant digit, e.g.

            [1,2,3] --> 1x10^2 + 2x10^1 + 3x10^0 = 123
    """
    digs = reversed(digits) if isinstance(digits, list) else digits
    i = 0
    n = 0        
    for d in digs:
        n += d*10**i
        i += 1
    return n


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


def primes(num_terms=None, int_range=None, ubound=None):
    """
        Generates all primes. Three mutually exclusive options exist: num_terms
        indicates the number of consecutive primes to generate, starting from 2;
        int_range indicates the range of positive integers within which the
        primes should be generated; ubound indicates a strict upper bound for
        the generated primes.
    """    
    if num_terms or int_range or ubound:
        if num_terms:
            n = 2
            i = 1
            while i <= num_terms:
                if is_prime(n):
                    yield n
                    i += 1
                n += 1
        elif int_range:
            for n in int_range:
                if is_prime(n):
                    yield n
        else:
            for n in range(1, ubound):
                if is_prime(n):
                    yield n
        return

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1        


def rotations(n):
    """
        Generates a sequence of (right) rotations of a given positive integer n.
    """
    digs = list(digits(n))
    n = len(digs)
    for i in range(n):
        yield sum(digs[(j + i) % n] * 10**j for j in range(n))
