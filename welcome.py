from kivy.uix.screenmanager import Screen
from kivy_garden.zbarcam import ZBarCam

class WelcomeScreen(Screen):
    def to_scanning(self):
        self.manager.current = 'scanning_screen'