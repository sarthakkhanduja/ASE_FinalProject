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
        self.create_database()
    
    def create_database(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS dbtransitwindsor;")
        self.mycursor.execute("USE dbtransitwindsor;")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS CustomerTable (FirstName varchar(50), LastName varchar(50), CardNumber varchar(16) PRIMARY KEY, phoneNumber varchar(10), isStudent INT, password varchar(50));")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS RidesTable (CardNumber varchar(16), Rides INT, LastRechargeID int, LastRide Date);")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS RechargeTable (LastRechargeID int NOT NULL AUTO_INCREMENT PRIMARY KEY, amount Double, LastRechargeDate Date, CreditCardNum varchar(16));")
        self.mydb.commit()
    
    def validateLogin(self, cardnumber, pwd):
        self.mycursor.execute(f"Select FirstName, LastName, CardNumber from CustomerTable WHERE CardNumber = '{cardnumber}' and password = '{pwd}'")
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False
    
    def getRidesAndLastRideFor(self, cardNumber) -> int:
        self.mycursor.execute(f"Select Rides, LastRide, LastRechargeID from RidesTable where CardNumber = '{cardNumber}' Order By LastRechargeID DESC")
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
    
    def updatePayment(self, amount, lastRechargeDate, creditCardNum):
        self.mycursor.execute(f"Insert into RechargeTable (amount, LastRechargeDate, CreditCardNum) values ('{amount}', '{lastRechargeDate}', '{creditCardNum}')")
        self.mydb.commit()
        self.mycursor.execute(f"Select LastRechargeID from RechargeTable where CreditCardNum = '{creditCardNum}' order by LastRechargeID DESC")
        result = self.mycursor.fetchall()
        if len(result):
            return result[0]
        else:
            return False
    
    def updateRides(self, bus_card_num, rides, lastRechageID, lastRechargeDate):
        self.mycursor.execute(f"Insert into RidesTable values ('{bus_card_num}', '{rides}', '{lastRechageID}', '{lastRechargeDate}');")
        self.mydb.commit()
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False
    
    def updateRideTaken(self, bus_card_num, rides):
        self.mycursor.execute(f"Update RidesTable Set Rides = '{rides}' where CardNumber = '{bus_card_num}');")
        self.mydb.commit()
        result = self.mycursor.fetchall()
        if len(result):
            return result
        else:
            return False

    

    

    






