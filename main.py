from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from welcome import WelcomeScreen
from scannerapp import ScanningScreen
from testpage import OutputScreen

import sqlite3
import sys
import traceback

##TODO : reduce scanning speed
##TODO : record value from scanning into database
##TODO : making signature screen after receiving shipment
##TODO : making signature screen before sending shipment
##TODO : record signature into database

##DOLATER : login page
##DOLATER : specific page for user login

pb = ProgressBar(max=10000)

class RootWidget(ScreenManager):
    Builder.load_file('design.kv')

class MainApp(App):
    def connectAppDatabase(self):
        pb.value = 750
        try:
            con = sqlite3.connect('./data/database.db')
            return con
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
    
    def readTable(self, con):
        cursorObj = con.cursor()
        try:
            cursorObj.execute("CREATE TABLE IF NOT EXIST scanning_data(ID integer PRIMARY KEY, PHYID text, PHYNUMBER integer, BRANCH NUMBER integer, BRANCH NAME integer)")
            con.commit()
        except sqlite3.OperationalError:
            print('Already did.')

    def build(self):
        con = self.connectAppDatabase()
        self.readTable(con)
        sm = RootWidget()
        return sm

if __name__ in "__main__":
    MainApp().run()