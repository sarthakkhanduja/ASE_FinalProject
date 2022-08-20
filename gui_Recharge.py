from cProfile import label
from curses import window
from datetime import date
import sys
import random
from datetime import date
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from database_creation import DbInitialser
from user import User

class RechargeWindow():
    def __init__(self, user:User, gui):
        self.gui = gui
        self.user = user
        self.db = DbInitialser()
        self.student = self.db.getIsStudent(self.user.cardNumber)
        self.amount = 0.0
        self.window = QWidget()
        self.window.setGeometry(200,200,550,550)
        self.window.setWindowTitle("Recharge")
        self.SignUp_GUI()
    
    def SignUp_GUI(self):
        label_CardNo = QLabel(self.window)
        label_CardNo.setText("Card Number: " + self.user.cardNumber)
        label_CardNo.setFont(QFont("Roboto", 18))
        #grid.addWidget(label_Name,0,0)
        label_CardNo.move(20,10)

        #Card number: <---- ---- ---- ---->
        self.label_CreditCard = QLabel(self.window)
        self.label_CreditCard.setText(" Credit Card No: ")
        self.label_CreditCard.setFont(QFont("Roboto", 13))
        self.label_CreditCard.move(20,80)

        #Card Number text box
        self.creditCardTextBox = QLineEdit(self.window)
        self.creditCardTextBox.move(190, 70)
        self.creditCardTextBox.resize(280,40)

        #Password : <---- ---- ---- ---->
        self.label_Password = QLabel(self.window)
        self.label_Password.setText("CVV : ")
        self.label_Password.setFont(QFont("Roboto", 13))
        self.label_Password.move(20,150)

        #Password text box
        self.passwordTextBox = QLineEdit(self.window)
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.move(190, 140)
        self.passwordTextBox.resize(280,40)

        #First Name
        self.label_expiryDate = QLabel(self.window)
        self.label_expiryDate.setText("Expiry Date: ")
        self.label_expiryDate.setFont(QFont("Roboto", 13))
        self.label_expiryDate.move(20,220)

        #First Name text box
        self.expiryDateTextBox = QLineEdit(self.window)
        self.expiryDateTextBox.move(190, 210)
        self.expiryDateTextBox.resize(60,40)

        self.label_expiryDateSlash = QLabel(self.window)
        self.label_expiryDateSlash.setText(" / ")
        self.label_expiryDateSlash.setFont(QFont("Roboto", 13))
        self.label_expiryDateSlash.move(250,215)

        self.expiryDateTextBox2 = QLineEdit(self.window)
        self.expiryDateTextBox2.move(270, 210)
        self.expiryDateTextBox2.resize(60,40)

        #Last Name
        self.label_Name = QLabel(self.window)
        self.label_Name.setText("Name on card: ")
        self.label_Name.setFont(QFont("Roboto", 13))
        self.label_Name.move(20,290)

        #Last Name text box
        self.NameTextBox = QLineEdit(self.window)
        self.NameTextBox.move(190, 280)
        self.NameTextBox.resize(280,40)

        #Phone Number
        self.label_phNo = QLabel(self.window)
        self.label_phNo.setText("No. of Rides: ")
        self.label_phNo.setFont(QFont("Roboto", 13))
        self.label_phNo.move(20,360)

        #Phone Number text box
        self.phNoTextBox = QLineEdit(self.window)
        self.phNoTextBox.move(190, 350)
        self.phNoTextBox.resize(280,40)
        self.phNoTextBox.textChanged.connect(self.calculateFinalAmount)

        self.label_Amt = QLabel(self.window)
        self.label_Amt.setText("Total Amount: " + str(self.amount))
        self.label_Amt.setFont(QFont("Roboto", 13))
        self.label_Amt.move(20,430)
        self.label_Amt.setGeometry(20, 390, 400, 100)


        #Submit Button
        self.button_login = QPushButton("Submit", self.window)
        self.button_login.setFont(QFont("Roboto", 10))
        self.button_login.setGeometry(150, 500, 100,50)
        

        #Cancel Button
        button_cancel = QPushButton("Cancel", self.window)
        button_cancel.setFont(QFont("Roboto", 10))
        button_cancel.setGeometry(310, 500, 100,50)
        button_cancel.clicked.connect(self.onCancelClick)
    
    def onCancelClick(self):
        self.window.close()

    def calculateFinalAmount(self):
        rides = self.phNoTextBox.text()

        if(rides == ''):
            rides_int = 0
        else:
            rides_int = int(rides)

        if(self.student):
            rideRate = 2.15
        else:
            rideRate = 3.15
        self.amount = rides_int * rideRate
        self.label_Amt.setText("Total Amount: " + str(self.amount))
    