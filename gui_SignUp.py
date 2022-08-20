from cProfile import label
from curses import window
from datetime import date
import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from database_creation import DbInitialser
from user import User

class SignUp():
    def __init__(self):
        self.Title = "Sign Up"
        # self.cardNo = "4544 5455 7877 8988"
        self.db = DbInitialser()
        self.window = QWidget()
        self.SignUp_GUI()
    
    def SignUp_GUI(self):
        self.window.setGeometry(200,200,550,550)
        self.window.setWindowTitle(self.Title)

        label_Name = QLabel(self.window)
        label_Name.setText("Hello, please fill the following details: ")
        label_Name.setFont(QFont("Roboto", 18))
        #grid.addWidget(label_Name,0,0)
        label_Name.move(20,10)

        #Card number: <---- ---- ---- ---->
        self.label_Card = QLabel(self.window)
        self.label_Card.setText("Card Number: ")
        self.label_Card.setFont(QFont("Roboto", 13))
        self.label_Card.move(20,80)

        #Card Number text box
        self.cardTextBox = QLineEdit(self.window)
        self.cardTextBox.move(170, 70)
        self.cardTextBox.resize(280,40)

        #Password : <---- ---- ---- ---->
        self.label_Password = QLabel(self.window)
        self.label_Password.setText("Password : ")
        self.label_Password.setFont(QFont("Roboto", 13))
        self.label_Password.move(20,150)

        #Password text box
        self.passwordTextBox = QLineEdit(self.window)
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.move(170, 140)
        self.passwordTextBox.resize(280,40)

        #First Name
        self.label_fName = QLabel(self.window)
        self.label_fName.setText("First Name: ")
        self.label_fName.setFont(QFont("Roboto", 13))
        self.label_fName.move(20,220)

        #First Name text box
        self.fNameTextBox = QLineEdit(self.window)
        self.fNameTextBox.move(170, 210)
        self.fNameTextBox.resize(280,40)

        #Last Name
        self.label_lName = QLabel(self.window)
        self.label_lName.setText("Last Name: ")
        self.label_lName.setFont(QFont("Roboto", 13))
        self.label_lName.move(20,290)

        #Last Name text box
        self.lNameTextBox = QLineEdit(self.window)
        self.lNameTextBox.move(170, 280)
        self.lNameTextBox.resize(280,40)

        #Phone Number
        self.label_phNo = QLabel(self.window)
        self.label_phNo.setText("Phone No.: ")
        self.label_phNo.setFont(QFont("Roboto", 13))
        self.label_phNo.move(20,360)

        #Phone Number text box
        self.phNoTextBox = QLineEdit(self.window)
        self.phNoTextBox.move(170, 350)
        self.phNoTextBox.resize(280,40)

        #Submit Button
        button_login = QPushButton("Submit", self.window)
        button_login.setFont(QFont("Roboto", 10))
        button_login.setGeometry(150, 450, 100,50)
        button_login.clicked.connect(self.onSubmitClick)

        #Cancel Button
        button_cancel = QPushButton("Cancel", self.window)
        button_cancel.setFont(QFont("Roboto", 10))
        button_cancel.setGeometry(310, 450, 100,50)
        button_cancel.clicked.connect(self.onCancelClick)
  
    
    def onCancelClick(self):
        self.window.close()
        
    def onSubmitClick(self):
        print(f"'{self.fNameTextBox.text()}','{self.lNameTextBox.text()}','{self.cardTextBox.text()}', '{self.phNoTextBox.text()}', '{random.randint(0,10)%2}', '{self.passwordTextBox.text()}'")
        values = (f"'{self.fNameTextBox.text()}','{self.lNameTextBox.text()}','{self.cardTextBox.text()}', '{self.phNoTextBox.text()}', '{random.randint(0,10)%2}', '{self.passwordTextBox.text()}'")
        self.db.addUser(values)
        self.window.close()
