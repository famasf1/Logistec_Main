from kivy.uix.screenmanager import Screen

class ScanningScreen(Screen):

    def to_mainpage(self):
        self.manager.current = 'welcome_screen'
    
    def readScan(self):
        print(self.parent.ids.reading_scan.text) 