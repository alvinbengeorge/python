from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button

import cv2

class CamApp(App):   

    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        self.number=1
        btn=Button(text="Click",pos_hint={'x':0,'y':.4},size_hint=(.1,.2))
        btn.bind(on_press=self.capt)
        layout.add_widget(btn)
        layout.add_widget(self.img1)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        self.buf1 = frame
        bu = cv2.flip(self.buf1, 0)
        buf = bu.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')        
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')        
        self.img1.texture = texture1
        
    def capt(self,event):
        cv2.imwrite(str(self.number)+".png",self.buf1)
        self.number+=1
        

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()
