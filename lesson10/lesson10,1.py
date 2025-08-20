from typing import Generator

def some_gen(begin:int, n:int, func)->Generator[int, None, None]:

    current = begin

    for _ in range(n):
        yield current
        current = func(current)

def pow2(x):
    return x ** 2

from inspect import isgenerator
gen = some_gen(2, 4, pow2)


# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')

print(list(some_gen(3,9,pow2)))