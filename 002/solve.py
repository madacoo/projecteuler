""" By considering the terms in the Fibonacci sequence whose values
    do not exceed four million, find the sum of the even-valued terms.
"""

def fibo_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

f = fibo_gen()
fibos = [0]
while fibos[-1] < 4000000:
    fibos.append(next(f))
print(sum([x for x in fibos if x % 2 == 0]))


