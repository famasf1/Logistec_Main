from kivy.uix.screenmanager import Screen
from kivy_garden import zbarcam
from kivy_garden.xcamera import XCamera

class ScanningScreen(Screen):

    def to_mainpage(self):
        self.manager.current = 'welcome_screen'

    def readBar(self):
        print(', '.join([str(symbol.data) for symbol in zbarcam.ZBarCam.symbols]))