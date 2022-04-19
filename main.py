from msilib.schema import Error
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.lang import Builder
from welcome import WelcomeScreen
from scannerapp import ScanningScreen

import sqlite3
from sqlite3 import Error

##TODO : add sound every time scanning is success
##TODO : record value from scanning into database
##TODO : making signature screen after receiving shipment
##TODO : making signature screen before sending shipment
##TODO : record signature into database

##DOLATER : login page
##DOLATER : specific page for user login

class RootWidget(ScreenManager):
    Builder.load_file('design.kv')

class MainApp(App):
    def connectAppDatabase(self):
        try:
            con = sqlite3.connect('./data/database.db')
            return con
        except Error:
            print(Error)
    
    def readTable(self, con):
        cursorObj = con.cursor()
        try:
            cursorObj.execute("CREATE TABLE IF NOT EXIST scanning_data(ID integer PRIMARY KEY, PHYID text, PHYNUMBER integer, BRANCH NUMBER integer, BRANCH NAME integer)")
        except sqlite3.OperationalError:
            print('Already did.')
        con.commit()

    def build(self):
        con = self.connectAppDatabase()
        self.readTable(con)
        sm = RootWidget()
        return sm

if __name__ in "__main__":
    MainApp().run()