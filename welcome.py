from kivy.uix.screenmanager import Screen

class WelcomeScreen(Screen):
    def to_scanning(self):
        self.manager.current = 'scanning_screen'