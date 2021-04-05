import sqlite3 as db
from sqlite3.dbapi2 import Error
from . import main
import bcrypt

"""https://stackoverflow.com/questions/33989770/login-script-using-python-and-sqlite"""

conn = db.connect("database.db")
cur = conn.cursor()

class Encryption:
    def __init__(self) -> None:

        self.salt = bcrypt.gensalt()

    def encrypt(self,pwd):
        hashed = bcrypt.hashpw(bytes(pwd,"utf-8"),self.salt)
        print(hashed)
        return hashed
    def decrypt(self,pwd,hashed_pwd):
        d_crypt = bcrypt.checkpw(bytes(pwd,"utf-8"),hashed_pwd)
        return d_crypt

class Check_db:
    def check_table_login(self,tablename=...):
        """CHECKS FOR LOGIN TABLE"""
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {tablename} 
        (name STRING, passwd STRING)""") #IF table doesn't exist, create new 

class Get_user:
    def get_usr(self,usr):
        self.usr = usr
        cur.execute("""SELECT * FROM Users 
        WHERE name = ? """, (self.usr))
        rows = cur.fetchall()
        return rows

class Register:
    """REGISTER NEW USER"""
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd

    def check(self):
        cur.execute("""SELECT * FROM Users 
        WHERE name = ? """, (self.username,))
        rows = cur.fetchall()
        if rows:
            return True
        else:
            self.register()
        return False
        
    def register(self):
        pwd = Encryption().encrypt(self.passwd)

        cur.execute(f"""INSERT INTO Users (name, passwd) 
        VALUES (?,?)""",(self.username,pwd))
        conn.commit()

class Login:
    """LOGIN USER"""
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login_user(self):
        # cur.execute("""SELECT * FROM Users 
        # WHERE name = ? AND passwd = ? """, (self.username,self.password))
        # rows = cur.fetchall()
        cur.execute("""SELECT * FROM Users 
        WHERE name = ? """, (self.username,))
        rows = cur.fetchall()
        hashed = rows[0][1]
        pwd = Encryption().decrypt(self.password,hashed)

        if len(rows) >0 and pwd == True:
            print("deucerto")
            return True
        return False

