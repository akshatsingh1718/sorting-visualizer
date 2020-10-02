import sys
import pygame
import random
from pygame.locals import *
pygame.init()

# window size
HEIGHT = 800
WIDTH = 1000
# colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 155)
PURPLE = (10, 60, 242)
PINK = (242, 10, 161)
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting  Visualization')
font = pygame.font.SysFont(None, 30)
pygame.display.update()

clock = pygame.time.Clock()
FPS = 60
class Sorting:
    '''
    Class for storing all types of sorting algos
    '''
    def quick_sort(self, array):
        '''
        Function to sort array using Quick Sort
        '''
        sortings = []
        def partition(low, high):
            i = low-1
            pivot = array[high]
            for j in range(low, high):
                sortings.append(array[:])
                if array[j] < pivot:
                    i += 1
                    array[j], array[i] = array[i], array[j]
            array[i+1], array[high] = array[high], array[i+1]
            sortings.append(array[:])
            return i+1

        def sort(low, high):
            if low < high:
                pi = partition(low, high)
                sort(low, pi-1)
                sortings.append(array[:])
                sort(pi+1, high)

        sort(0, len(array)-1)
        return sortings

    def selection_sort(self, array):
        '''
        Selection sort
        '''
        sortings = []
        for i, _ in enumerate(array):
            sortings.append(array[:])
            min_index = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            array[min_index], array[i] = array[i], array[min_index]
        print(len(sortings))
        return sortings

    def insertion_sort(self, array):
        '''
        Insertion sort
        '''
        sortings = []
        for i in range(1, len(array)):
            sortings.append(array[:])
            key = array[i]
            j = i-1
            while j>=0 and array[j] > key:
                sortings.append(array[:])
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        sortings.append(array[:])
        print(len(array))
        return sortings

    def mergesort(self, array):
        '''
        Function to sort array using MergeSort
        '''
        def sort(array, l, r, sortings):
            mid = (l + r)//2
            if l < r:
                sort(array, l, mid, sortings)
                sort(array, mid + 1, r, sortings)
                sortings = merge(array, l, mid, mid + 1, r, sortings)
            return sortings

        def merge(array, x1, y1, x2, y2, sortings):
            i = x1
            j = x2
            temp = []
            while i <= y1 and j <= y2:
                if array[i] < array[j]:
                    temp.append(array[i])
                    i += 1
                else:
                    temp.append(array[j])
                    j += 1
            while i <= y1:
                temp.append(array[i])
                i += 1
            while j <= y2:
                temp.append(array[j])
                j += 1
            j = 0
            for i in range(x1, y2 + 1):
                sortings.append(array[:])
                array[i] = temp[j]
                j += 1
            sortings.append(array[:])
            return sortings

        sortings = []
        return sort(array, 0, len(array)-1, sortings)


    def bubble_sort(self, array):
        '''
        Function to sort array using BubblSort
        '''
        sortings = []
        for i, _ in enumerate(array):
            for j in range(i+1, len(array)):
                if array[i] > array[j]:
                    sortings.append(array[:])
                    array[i], array[j] = array[j], array[i]
        print(len(sortings))
        sortings.append(array[:])
        return sortings


def display_lines(sortings):
    '''
    Function to show lines as array elements to show visually
    how Bubble Sort works
    '''
    color = RED
    for i, arr in enumerate(sortings):
        color = GREEN if i == len(sortings)-1 else RED
        gameWindow.fill(BLACK)
        draw_array(arr, color)
        pygame.display.update()
        pygame.time.wait(10)

def draw_array(arr, color):
    rect_x_start = 200
    rect_x, rect_y = rect_x_start, 100
    rect_width = 4
    rect_width_inc = rect_width+3
    gameWindow.fill(BLACK)
    for _, num in enumerate(arr):
        rect = pygame.Rect(rect_x, rect_y, rect_width, num)
        pygame.draw.rect(gameWindow, color, rect, 0)
        rect_x += rect_width_inc


def random_array():
    '''
    Function to create a random unsorted array
    '''
    random_array = []
    for _ in range(1, 100):
        random_array.append(random.randrange(100, 600))
    #print(random_array)
    return random_array

def display_sorting_labels():
    sortings = ['RandomArray', 'QuickSort', 'BubbleSort', 'MergeSort', 'InsertionSort', 'SelectionSort']
    sort_name_rect = []
    input_x, input_y = 10, 100
    for sort_name in sortings:
        surface = font.render(sort_name, True, PINK)
        text_rect = pygame.Rect(input_x, input_y, surface.get_width()+10, 32)
        pygame.draw.rect(gameWindow, PURPLE, text_rect, 2)
        gameWindow.blit(surface, (text_rect.x+5, text_rect.y+5))
        input_y += 10+ text_rect.h
        sort_name_rect.append((text_rect, sort_name))
    return sort_name_rect

def gameloop():
    '''
    Main game loop to start pygame loop for using events.
    '''
    arr = random_array()
    is_sorting = False
    sorting = Sorting()
    draw_array(arr, GREEN)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not is_sorting:
                for sort_rect, name in sort_rect_names:
                    if sort_rect.collidepoint(event.pos):
                        print(name)
                        if name == 'QuickSort':
                            sortings = sorting.quick_sort(arr)
                            is_sorting = True
                        elif name == 'BubbleSort':
                            sortings = sorting.bubble_sort(arr)
                            is_sorting = True
                        elif name == 'MergeSort':
                            print('MergeSort')
                            sortings = sorting.mergesort(arr)
                            is_sorting = True
                        elif name == 'InsertionSort':
                            sortings = sorting.insertion_sort(arr)
                            is_sorting = True
                        elif name == 'SelectionSort':
                            sortings = sorting.selection_sort(arr)
                            is_sorting = True
                        elif name == 'RandomArray':
                            arr = random_array()
                            draw_array(arr, GREEN)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        sort_rect_names = display_sorting_labels()
        if is_sorting:
            arr = random_array()
            display_lines(sortings)
            is_sorting = False
        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    gameloop()
