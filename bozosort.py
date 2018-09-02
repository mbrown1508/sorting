from random import randint
from constants import *

# Generator
def bozo_sort_generator(array):
    sorted = False
    while not sorted:
        a = randint(0,len(array)-1)
        b = randint(0,len(array)-1)

        array[a], array[b] = array[b], array[a]

        yield MOVE, array, a, b

        sorted = True
        for x in range(len(array)-1):
            yield COMPARE, array, x, x + 1
            if array[x] > array[x+1]:
                sorted = False
                break

    yield COMPLETE, array, -1, -1