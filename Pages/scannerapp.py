from kivymd.uix.screen import MDScreen
from kivy.core.audio import SoundLoader

#ID
#PHY_ID
#PHY_NUMBER
#BRANCH_NUMBER
#BRANCH_NAME

beep = SoundLoader.load('Asset/beep.wav')
if beep:
    print('Sound Found!')

class ScanningScreen(MDScreen):

    def to_mainpage(self):
        self.manager.current = 'welcome_screen'
        beep.unload()
    
    def readScan(self):
        foundBarcode = str(self.ids['reading_scan'].text).translate({ord(i): None for i in f"b'A00"})
        if foundBarcode:
            foundBarcode = str(foundBarcode).split("-")
            ####### RUN SQL INSERT HERE ######
            #MainApp.build.cursorObj.execute('''INSERT OR IGNORE INTO print_Data ()''')
            #MainApp.build.cursorObj.commit()
            #self.manager.current = 'signature_screen'

    def to_signature(self):
        self.manager.current = 'signature_screen'
        beep.unload()



