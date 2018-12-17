""" What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """


def has_factors(factor, n):
    """ Return True if n is divisible by all f < factor. """
    for f in range(2, factor):
        if n % f != 0: return False
    return True


x = n = 20
while not has_factors(n, x):
    x += n
print(x)
