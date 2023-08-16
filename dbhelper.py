import mysql.connector
import sys
class DBhelper:

    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="",database="flipkart")
            self.cur=self.con.cursor()
        except:
            print("some error occured")
            sys.exit(0)
        else:  
            print("connected to database")
    # REgister..........................................
    def register(self,name,email,password):
        try:
            self.cur.execute("INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');".format(name,email,password))
            self.con.commit()
        except:
            return -1
        else:
            return 1
    # searching........
    def search(self,email,password):
        self.cur.execute("SELECT *FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
        data=self.cur.fetchall()
        return data
        
