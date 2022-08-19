import mysql.connector

class DbInitialser:

    def __init__(self) -> None:
        self.open_connection()

    def open_connection(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="admin@1234"
            )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("USE dbtransitwindsor;")
    
    def create_database(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS dbtransitwindsor;")
        self.mycursor.execute("USE dbtransitwindsor;")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS CustomerTable (FirstName varchar(50), LastName varchar(50), CardNumber varchar(16) PRIMARY KEY, phoneNumber varchar(10), isStudent INT, password varchar(50));")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS RidesTable (CardNumber varchar(16) PRIMARY KEY, Rides INT, LastRechargeID INT, LastRide Date);")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS RechargeTable (LastRechargeID INT PRIMARY KEY, amount Double, LastRechargeDate Date);")
        self.mydb.commit()
    
    def validateLogin(self, cardnumber, pwd):
        self.mycursor.execute(f"Select FirstName, LastName, CardNumber from CustomerTable WHERE CardNumber = '{cardnumber}' and password = '{pwd}'")
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False
    
    def getRidesAndLastRideFor(self, cardNumber) -> int:
        self.mycursor.execute(f"Select Rides, LastRide, LastRechargeID from RidesTable where CardNumber = '{cardNumber}' order by LastRechargeID DESC")
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False
    
    def getLastRideDateFor(self, lastRechargeID) -> int:
        self.mycursor.execute(f"Select LastRechargeDate from RechargeTable where LastRechargeID = '{lastRechargeID}'")
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False
    
    def addUser(self, values):
        self.mycursor.execute(f"Insert into CustomerTable values ({values})")
        self.mydb.commit()
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False
        
    def getIsStudent(self, cardNum) -> bool:
        self.mycursor.execute(f"Select isStudent from CustomerTable where CardNumber = '{cardNum}'")
        result = self.mycursor.fetchall()
        if result[0]:
            return True
        else:
            return False
    
    def updatePayment(self, values):
        self.mycursor.execute(f"Insert into RechargeTable values ({values})")
        self.mydb.commit()
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False
    
    def updateRides(self, bus_card_num, rides, lastRechageID):
        self.mycursor.execute(f"Insert into RidesTable values ('{bus_card_num}, '{rides}', '{lastRechageID}');")
        self.mydb.commit()
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False

    

    

    






