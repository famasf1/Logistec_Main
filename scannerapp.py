from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader

beep = SoundLoader.load('Asset/beep.wav')
if beep:
    print('Sound Found!')

class ScanningScreen(Screen):

    def to_mainpage(self):
        self.manager.current = 'welcome_screen'
        beep.unload()
    
    def readScan(self):
        foundBarcode = str(self.ids['reading_scan'].text).translate({ord(i): None for i in f"b'A00"})
        if foundBarcode:
            self.manager.current = 'output_screen'
            beep.play()