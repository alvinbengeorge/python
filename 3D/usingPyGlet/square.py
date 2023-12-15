from pyglet import shapes
from random import randint
from multiprocessing import Pool

def square(x: int, y: int) -> shapes.Rectangle: 
    return shapes.Rectangle(x, y, 50, 50, color=(randint(0, 255), 0, 0))

def gridGenerator(window):
    for x in range(0, int(window.width), 50):
        for y in range(0, int(window.height), 50):
            square(x, y).draw()