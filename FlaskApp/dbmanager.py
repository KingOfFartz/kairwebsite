from dotenv import load_dotenv
import os
import mysql.connector
import requests
from mysql.connector import errorcode

load_dotenv()
dbfile = os.getenv('DATABASE_FILE')

class DbManager:
    def __init__(self):
         self.conn = self.getDatabase()

    def getDatabase(self):
        try:
            print(dbfile)
            conn = mysql.connector.connect(
                    host='localhost',
                    user='flaskapp',
                    port='3306',
                    password='LetMeInKelownaAir',
                    database=dbfile)
            print(conn)
            return conn
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Wrong user name, password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                print(err)
            else:
                print(err)


               
