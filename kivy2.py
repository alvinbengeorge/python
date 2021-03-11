from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Rectangle,Line
class MyLabel(Label):
    def __init__(self,text):
        super().__init__()
        self.text=text
    def on_touch_down(self,touch):
        print("Down",touch.pos)
        self.canvas.add(Rectangle(pos=touch.pos,size=(2,2)))
    def on_touch_up(self,touch):
        print("Up",touch.pos)
    def on_touch_move(self,touch):
        print("move",touch.pos)
        self.canvas.add(Rectangle(pos=touch.pos,size=(2,2)))
class MyApp(App):
    def build(self):
        self.thislabel=MyLabel('hi')
        return self.thislabel


if __name__=='__main__':
    MyApp().run()
