from random import randint, shuffle
import sys, pygame
from bubblesort import bubble_sort_generator
from itersort import iter_sort_generator
from bozosort import bozo_sort_generator
from radixsort import radix_sort_generator
from mergesort import merge_sort_generator
from selectionsort import selection_sort_generator
from constants import *

import time

algorithm = radix_sort_generator

iterations_per_loop = 1
length = 100
min = 0
max = 10000


unsorted_array = list(randint(0, max) for _ in range(length))
#unsorted_array = list(range(length))
shuffle(unsorted_array)
#unsorted_array = reverse
#unsorted_array = sorted

size = width, height = 1000, 600
line_width = int(width/length)
scale = height / max

black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0


pygame.init()
screen = pygame.display.set_mode(size)

generator = algorithm(unsorted_array)

state = START

while 1:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    i_list = []
    j_list = []

    for _ in range(iterations_per_loop):
        if state != COMPLETE:
            state, sorted_array, i, j = next(generator)
            i_list.append(i)
            j_list.append(j)

    screen.fill(black)

    for x, element in enumerate(sorted_array):
        color = white
        if x in i_list or x in j_list:
            if state == MOVE:
                color = red
            else:
                color = green

        pygame.draw.line(screen, color,(line_width/2+(x*line_width),height), (line_width/2+(x*line_width),height-(element*scale)), line_width)

    pygame.display.flip()
