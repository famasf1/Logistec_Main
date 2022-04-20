from kivy.uix.screenmanager import Screen

class ScanningScreen(Screen):

    def to_mainpage(self):
        self.manager.current = 'welcome_screen'
    
    def test_print(self):
        print(self.ids.reading_scan.text)