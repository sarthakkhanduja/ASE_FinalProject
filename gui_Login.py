from cProfile import label
from curses import window
from curses.ascii import US
from datetime import date
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from database_creation import DbInitialser
from gui import DashBoard
from user import User
from gui_SignUp import SignUp

class LoginWindow():
    def __init__(self):
        self.Title = "Login Window"
        self.db = DbInitialser()
        # self.db.open_connection()
        # self.db.create_database()
        self.app = QApplication([])
        self.window = QWidget()
        self.LoginWindow_GUI()
        self.window.show()
        self.app.exec_()
    
    def LoginWindow_GUI(self):
        self.window.setGeometry(200,200,450,350)
        self.window.setWindowTitle("Login")

        label_Name = QLabel(self.window)
        label_Name.setText(" Welcome to transit windsor ")
        label_Name.setFont(QFont("Roboto", 22))
        #grid.addWidget(label_Name,0,0)
        label_Name.move(20,10)

        #Card number: <---- ---- ---- ---->
        self.label_Card = QLabel(self.window)
        self.label_Card.setText("Card Number: ")
        self.label_Card.setFont(QFont("Roboto", 13))
        self.label_Card.move(20,80)

        #Card Number text box
        self.cardTextBox = QLineEdit(self.window)
        self.cardTextBox.move(150, 70)
        self.cardTextBox.resize(280,40)

        #Password : <---- ---- ---- ---->
        self.label_Password = QLabel(self.window)
        self.label_Password.setText("Password : ")
        self.label_Password.setFont(QFont("Roboto", 13))
        self.label_Password.move(20,150)

        #Password text box
        self.passwordTextBox = QLineEdit(self.window)
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.move(150, 140)
        self.passwordTextBox.resize(280,40)

        #Login Button
        button_login = QPushButton("Login", self.window)
        button_login.setFont(QFont("Roboto", 10))
        button_login.setGeometry(150, 200, 100,50)
        button_login.clicked.connect(self.onLoginClick)

        #Cancel Button
        button_cancel = QPushButton("Cancel", self.window)
        button_cancel.setFont(QFont("Roboto", 10))
        button_cancel.setGeometry(310, 200, 100,50)
        button_cancel.clicked.connect(self.onCancelClick)

        #Signup Button
        signup_button = QPushButton("New User?", self.window)
        signup_button.setFont(QFont("Roboto", 10))
        signup_button.setGeometry(175, 275, 200,50)
        signup_button.clicked.connect(self.onSignupClick)

  
    def onSignupClick(self):
        self.signUpWindow = SignUp()
        self.signUpWindow.window.show()
    
    def onCancelClick(self):
        self.app.close()
        
    def onLoginClick(self):
        card_num = self.cardTextBox.text()
        pwd = self.passwordTextBox.text()
        result = self.db.validateLogin(card_num, pwd)
        if result == False:
            msg = QMessageBox()
            msg.setText("Incorrect card number or password")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
        else:
            print(result)
            (firstName, lastName, cardNumber) = result[0]
            user = User(firstName, lastName, cardNumber)
            self.window.close()
            self.dashboard = DashBoard(user)
            self.dashboard.getWindow().show()


myWindow = LoginWindow()