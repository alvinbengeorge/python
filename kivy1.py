from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.c=1
    def up(self,c):
        self.c+=1
        print(self.c)
    def down(self,c):
        self.c-=1
        print(self.c)
    def build(self):
        st=str(self.c)
        layout=FloatLayout()
        self.l1=Label(text=st,size_hint=(1,1),pos_hint={'center_x':0.5,'center_y':0.9})
        self.l2=Button(text="increment",size_hint=(1,0.1))
        self.l3=Button(text="decrement",size_hint=(1,0.1),pos_hint={'center_x':0.5,'center_y':0.15})
        self.l2.bind(on_press=self.up)
        self.l3.bind(on_press=self.down)
        layout.add_widget(self.l1)
        layout.add_widget(self.l2)
        layout.add_widget(self.l3)
        return layout


if __name__=='__main__':
    MyApp().run()
