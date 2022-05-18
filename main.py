from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from welcome import WelcomeScreen
from scannerapp import ScanningScreen

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
            con = sqlite3.connect('data\database.db')
            return con
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        
    def build(self):
        con = self.connectAppDatabase()
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXISTS scanning_data (ID INTEGER PRIMARY KEY, PHY_ID TEXT, PHY_NUMBER INTEGER, BRANCH_NUMBER INTEGER, BRANCH_NAME INTEGER)")
        con.commit()
        sm = RootWidget()
        return sm

if __name__ in "__main__":
    MainApp().run()