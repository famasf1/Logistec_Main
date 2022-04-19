from kivy.uix.screenmanager import Screen
from kivy_garden.zbarcam import ZBarCam
from kivy_garden.xcamera import XCamera

class ScanningScreen(Screen):
    def to_mainpage(self):
        self.manager.current = 'welcome_screen'