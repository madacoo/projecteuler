""" What is the largest prime factor of the number 600851475143 ? """

from math import sqrt

def is_prime(n):
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True


def largest_prime_factor(n):
    for x in range(int(sqrt(n))+1, 2, -1):
        if n % x == 0 and is_prime(x):
            return x

print(largest_prime_factor(600851475143))

    
