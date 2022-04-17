from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.lang import Builder
from welcome import WelcomeScreen
from scannerapp import ScanningScreen

##TODO : add sound every time scanning is success
##TODO : record value from scanning into database
##TODO : making signature screen after receiving shipment
##TODO : making signature screen before sending shipment
##TODO : record signature into database

##DOLATER : login page
##DOLATER : specific page for user login


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