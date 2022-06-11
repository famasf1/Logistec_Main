from kivy.uix.screenmanager import Screen

class OutputScreen(Screen):
    def showString(self):
        foundBarcode = str(self.ids['reading_scan'].text).translate({ord(i): None for i in f"b'A00"})
        if foundBarcode:
            print(foundBarcode)