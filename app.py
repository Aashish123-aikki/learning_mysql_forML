import sys
from dbhelper import DBhelper
class flipkart:

    def __init__(self):
        # connect to db
        self.db=DBhelper()
        self.menu()
    def menu(self):
        inp=input("Enter:\n 1. To register \n2. To Login\n3. Anything else to exit")
        if inp=="1":
            self.register()
        elif inp=="2":
            self.login()
        else:
            sys.exit(1000)
    # Registering user.....................................
    def register(self):
        name=input("Enter name")
        email=input("enter email")
        passw=input("enter password")
        response=self.db.register(name,email,passw)
        if response:
            print("Sucessfully registered")
            self.menu()
        else:
            print("Error occured!")
    def login(self):
        email=input("enter email")
        passw=input("enter password")
        data=self.db.search(email,passw)
        if len(data)==0:
            print("Incorrect email/password")
            self.login()
        else:
            print("Hello '{}'".format(data[0][1]))
a=flipkart()