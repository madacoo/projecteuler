""" Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """


def sum_squares(n):
    return sum([i*i for i in range(n+1)])


def square_sum(n):
    x = sum(range(n+1))
    return x*x


n = 100
print(square_sum(n) - sum_squares(n))
