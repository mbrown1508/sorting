from random import randint, seed
from timeit import timeit
from tabulate import tabulate
from bubblesort import bubble_sort
from itersort import iter_sort
from radixsort import radix_sort
from mergesort import merge_sort
from constants import *

seed(1000)

iterations = 10
arrays = 10
length = 1000

unsorted_array_short = [3,4,8,1,9,6,5,0]
unsorted_array_long = [[randint(0,length) for _ in range(length)] for x in range(arrays)]


def wrapper(func, *args):
    def wrapped():
        return [func(x[:]) for x in args[0]]
    return wrapped

variations = [iter_sort, bubble_sort, radix_sort, merge_sort, sorted]
str_variations = ['iter_sort', 'bubble_sort', 'radix_sort', 'merge_sort','builtin']

table = []
for i, (name, variation) in enumerate(zip(str_variations, variations)):
    table.append([name])

    wrapped = wrapper(variation, unsorted_array_long)
    result = timeit(wrapped, number=iterations)
    table[i].append('{:.4f}ms'.format(result/iterations*1000/arrays))

print(tabulate(table, headers=['Algorithim', 'Time']))