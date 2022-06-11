from kivy.uix.screenmanager import Screen

class WelcomeScreen(Screen):
    def to_scanning(self):
        self.manager.current = 'scanning_screen'

    def readTable(self, con):
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXIST scanning_data (ID integer PRIMARY KEY, PHYID text, PHYNUMBER integer, BRANCH NUMBER integer, BRANCH NAME integer)")
        con.commit()