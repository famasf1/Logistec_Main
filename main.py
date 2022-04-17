from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.lang import Builder
from welcome import WelcomeScreen
from scannerapp import ScanningScreen

Builder.load_file('design.kv')

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        sm = RootWidget()
        sm.add_widget(WelcomeScreen())
        sm.add_widget(ScanningScreen())   
        return sm

if __name__ in "__main__":
    MainApp().run()