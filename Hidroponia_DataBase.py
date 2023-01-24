import mysql.connector
from mysql.connector import Error

class Hidroponia:
    def __init__(self):
        self.connection = connection = mysql.connector.connect(host='localhost', user= 'root', passwd='groot', db='hidroponia' )
    