#<stdio>
import sqlite3
import sys
import traceback

### Kivy
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp

### Import page to work with ScreenManager.
# Factory class will automatically go to each page and grab Screen class.
# From individual files.
# This is for future scaling and readability purpose. Though i don't know if this
# is even remotely Pythonic.
from Pages.scannerapp import ScanningScreen
from Pages.signaturepage import SignatureScreen
from Pages.welcome import WelcomeScreen

##TODO : reduce scanning speed
##TODO : record value from scanning into database
##TODO : making signature screen after receiving shipment
##TODO : making signature screen before sending shipment
##TODO : record signature into database

##DOLATER : login page
##DOLATER : specific page for user login

class RootWidget(ScreenManager):
    Builder.load_file('design.kv')

class LogistecApp(MDApp):
    def connectAppDatabase(self):
        try:
            con = sqlite3.connect('data\database.db')
            return con
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        
    ### FPS MONITORING FOR DEBUGGING AND PERFORMANCE TESTING PURPOSE ###
    # PLEASE DELETE IT BEFORE COMPLILING #
    def on_start(self):
        self.fps_monitor_start()

    def build(self):
        con = self.connectAppDatabase()
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXISTS scanning_data (ID INTEGER PRIMARY KEY, PHY_ID TEXT, PHY_NUMBER INTEGER, BRANCH_NUMBER INTEGER, BRANCH_NAME INTEGER)")
        con.commit()
        sm = RootWidget()
        return sm

if __name__ in "__main__":
    LogistecApp().run()
