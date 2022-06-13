from kivymd.uix.screen import MDScreen
from kivy_garden.zbarcam.zbarcam import ZBarCam

class WelcomeScreen(MDScreen):
    def to_scanning(self):
        self.manager.current = 'scanning_screen'

    def readTable(self, con):
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXIST scanning_data (ID integer PRIMARY KEY, PHYID text, PHYNUMBER integer, BRANCH NUMBER integer, BRANCH NAME integer)")
        con.commit()