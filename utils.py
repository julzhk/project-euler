def digits(n):
    """
        Generates the sequence of digits of a given integer n,
        starting from the least significant digit.
    """
    m = n
    while m:
        d = m % 10
        yield d
        m //= 10


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


def rotations(n):
    """
        Generates a sequence of (right) rotations of a given positive integer n.
    """
    digs = list(digits(n))
    n = len(digs)
    for i in range(n):
        yield sum(digs[(j + i) % n] * 10**j for j in range(n))
