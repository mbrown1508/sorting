from random import randint, shuffle, seed

seed(1000)

already_sorted = list(range(100))
reverse = list(range(99,-1,-1))
shuffle_array = list(range(100))
shuffle_arrays = []

for _ in range(5):
    shuffle(shuffle_array)
    shuffle_arrays.append(shuffle_array[:])

COMPARE = 0
MOVE = 1
COMPLETE = 2
START = -1

