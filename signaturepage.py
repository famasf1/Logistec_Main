from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

class SignatureScreen(Screen):
    def draw_size(self):
        d = 30.
        return d
    def touch_down(self, touch):
        return touch