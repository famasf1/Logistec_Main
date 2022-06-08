from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class SignatureScreen(Screen):
    def draw_size(self):
        d = 30.
        return d

    def ontouch(self, touch):
        return touch