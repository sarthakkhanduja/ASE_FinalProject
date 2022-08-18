import mysql.connector

class DbInitialser:

    def open_connection(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin@1234"
            )
        self.mycursor = self.mydb.cursor()
    
    def create_database(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS dbtransitwindsor;")
        self.mycursor.execute("USE dbtransitwindsor;")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS CustomerTable (FirstName varchar(50), LastName varchar(50), CardNumber varchar(12) PRIMARY KEY, phoneNumber varchar(10), isStudent INT, password varchar(50));")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS RidesTable (CardNumber varchar(12) PRIMARY KEY, Rides INT, LastRechargeID INT FOREIGN KEY, LastRide Date);")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS RidesTable (LastRechargeID PRIMARY KEY INT, amount Double, LastRechargeDate Date);")
        self.mydb.commit()
    
    def validateLogin(self, cardnumber, pwd):
        self.mycursor.execute(f"Select * from CustomerTable where CardNumber = {cardnumber} and password = {pwd}")
        result = self.mycursor.fetchall()
        print(result)

    

    

    






