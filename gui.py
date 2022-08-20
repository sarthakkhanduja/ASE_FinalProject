from cProfile import label
from curses import window
from datetime import date
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from database_creation import DbInitialser
from user import User
from gui_Recharge import RechargeWindow
import random

class DashBoard:

    def __init__(self, user:User) -> None:
        self.user = user
        self.db = DbInitialser()
        self.window = QWidget()
        self.window.setGeometry(200,200,850,500)
        self.window.setWindowTitle("Transit App")
        self.loadWindow()
    
    def getWindow(self):
        return self.window
    
    def loadWindow(self):
        self.window = QWidget()
        #Hello, <name>
        self.label_Name = QLabel(self.window)
        self.label_Name.setText("Hello, " + self.user.firstName)
        self.label_Name.setFont(QFont("Roboto", 22))
        #grid.addWidget(label_Name,0,0)
        self.label_Name.move(20,10)

        #Card number: <---- ---- ---- ---->
        self.label_Card = QLabel(self.window)
        self.label_Card.setText("Card Number: " + self.user.cardNumber)
        self.label_Card.setFont(QFont("Roboto", 13))
        self.label_Card.move(20,70)

        #Number of Rides
        self.label_RidesNo = QLabel(self.window)
        self.label_RidesNo.setText(str(self.user.ridesLeft))
        self.label_RidesNo.setFont(QFont("Roboto", 34))
        self.label_RidesNo.move(120, 180)

        #Rides Label
        self.label_Rides = QLabel(self.window)
        self.label_Rides.setText("Number of Rides Left")
        self.label_Rides.setFont(QFont("Roboto", 12))
        self.label_Rides.move(40, 260)

        #Last Ride Date
        self.label_RidesNo = QLabel(self.window)
        self.label_RidesNo.setText(str(self.user.lasRideDate))
        self.label_RidesNo.setFont(QFont("Roboto", 24))
        self.label_RidesNo.move(310, 190)

        #Last Ride Label
        label_Rides = QLabel(self.window)
        label_Rides.setText("Last Ride")
        label_Rides.setFont(QFont("Roboto", 12))
        label_Rides.move(370, 260)

        #Last Recharge Date
        self.label_RidesNo = QLabel(self.window)
        self.label_RidesNo.setText(str(self.user.lastRechargeDate))
        self.label_RidesNo.setFont(QFont("Roboto", 24))
        self.label_RidesNo.move(590, 190)

        #Last Recharge Label
        self.label_Rides = QLabel(self.window)
        self.label_Rides.setText("Last Recharge")
        self.label_Rides.setFont(QFont("Roboto", 12))
        self.label_Rides.move(630, 260)

        #Edit Account Button
        self.button_editAc = QPushButton("Edit Account", self.window)
        self.button_editAc.setFont(QFont("Roboto", 10))
        self.button_editAc.setGeometry(40, 400, 200,50)

        #ERecharge Button
        self.button_Recharge = QPushButton("Recharge", self.window)
        self.button_Recharge.setFont(QFont("Roboto", 10))
        self.button_Recharge.setGeometry(310, 400, 200,50)
        self.button_Recharge.clicked.connect(self.onRechargeClick)

        #NFC Button
        self.button_NFC = QPushButton("NFC", self.window)
        self.button_NFC.setFont(QFont("Roboto", 10))
        self.button_NFC.setGeometry(590, 400, 200,50)
        self.button_NFC.clicked.connect(self.onNFCClick)
    
    def onRechargeClick(self):
        print("called")
        self.newwindow = RechargeWindow(self.user, self)
        self.newwindow.button_login.clicked.connect(self.onSubmitClick)
        self.newwindow.window.show()
    
    def onSubmitClick(self):
        lastRechargeDate = date.today()
        rides = int(self.user.ridesLeft) + int(self.newwindow.phNoTextBox.text())
        amount = self.newwindow.amount
        card_num = self.newwindow.creditCardTextBox.text()
        lastRechargeID = self.db.updatePayment(amount, lastRechargeDate, card_num)
        self.db.updateRides(card_num, rides, lastRechargeID, lastRechargeDate)
        self.user.ridesLeft = str(rides)
        self.user.lastRechargeDate = lastRechargeDate
        self.window.hide()
        self.loadWindow()
        self.window.update()
        self.window.show()
        # self.db.updateRides(self.user.cardNumber,rides,lastRechargeID)
        self.newwindow.window.close()

    def onNFCClick(self):
        msg = QMessageBox()
        if int(self.user.ridesLeft) == 0:
            msg.setText("Please recharge for the ride")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            return
        else:
            msg.setText("Successfully validated")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        self.user.ridesLeft = str(int(self.user.ridesLeft) - 1)
        self.user.lasRideDate = date.today()
        self.db.updateRideTaken(self.user.cardNumber, self.user.ridesLeft)
        self.loadWindow()
        self.window.update()
        self.window.show()

    