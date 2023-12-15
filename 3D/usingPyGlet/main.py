import pyglet
import square

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    square.gridGenerator(window)

pyglet.app.run()