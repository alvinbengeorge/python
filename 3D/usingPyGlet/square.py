from pyglet import shapes
from pyglet.graphics import Batch
from random import randint
from time import time

SIZE = 10

def square(x: int, y: int, batch = None) -> shapes.Rectangle: 
    return shapes.Rectangle(x, y, SIZE, SIZE, color=(randint(0, 255), 0, 0), batch=batch)

def gridGenerator(window):
    start = time()
    for x in range(0, int(window.width)-int(SIZE//2), SIZE):
        batch = Batch()
        squares = columnGeneration(window, x, batch=batch)
        # print(squares)
        batch.draw()
    print(f"Time taken: {time()-start}")

def columnGeneration(window, x, batch):
    squares = []
    for y in range(0, int(window.height)-int(SIZE//2), SIZE):
        squares.append(square(x, y, batch=batch))
    return squares

if __name__ == "__main__":
    import main