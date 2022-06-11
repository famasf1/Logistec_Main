from kivymd.uix.screen import MDScreen
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line


class SignatureScreen(MDScreen):
    def to_scanning_page(self): #GO BACK TO SCANNING
        self.manager.current = 'scanning_screen'
    
    def clear_canvas(self, obj):
        obj = self.ids['signature_box']
        obj.canvas.clear()

class SignatureBox(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 0)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


