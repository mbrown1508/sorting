from random import randint
import sys, pygame

length = 100

min = 0
max = 500

size = width, height = 1000, 600
line_width = int(width/length)
scale = height / max

black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0

COMPARE = 0
MOVE = 1
COMPLETE = 2
START = -1

unsorted_array_short = [3,4,8,1,9,6,5,0]
unsorted_array_long = [randint(0,max) for _ in range(length)]


def bubble_sort_draw(array):
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                yield COMPARE, array, i, j
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
                yield MOVE, array, i, j
            else:
                yield COMPARE, array, i, j

    yield COMPLETE, array, -1, -1


def actual_bubble_sort_draw(array):
    for i in range(len(array)-1):
        swapped = False
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                swapped = True
                yield COMPARE, array, j, j + 1
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                yield MOVE, array, j, j + 1
            else:
                yield COMPARE, array, j, j + 1
        if not swapped:
            yield COMPLETE, array, -1, -1
    yield COMPLETE, array, -1, -1


pygame.init()
screen = pygame.display.set_mode(size)

generator = actual_bubble_sort_draw(unsorted_array_long)

state = START

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if state != COMPLETE:
        state, sorted_array, i, j = next(generator)

    screen.fill(black)

    for x, element in enumerate(sorted_array):
        color = white
        if x == i or x == j:
            if state == COMPARE:
                color = green
            else:
                color = red

        pygame.draw.line(screen, color,(line_width/2+(x*line_width),height), (line_width/2+(x*line_width),height-(element*scale)), line_width-1)

    pygame.display.flip()