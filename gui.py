from cProfile import label
from curses import window
from datetime import date
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    #Global variables
    fName = "Sarthak Khanduja"
    cardNo = "4456 0211 6458 9899"
    noOfRides = "9"
    lastRide = str(date(2022, 8, 10))
    lastRecharge = str(date(2022, 7, 19))

    #Main App and Window
    app = QApplication([])
    window = QWidget()
    window.setGeometry(200,200,850,500)
    window.setWindowTitle("Transit App")

    #Hello, <name>
    label_Name = QLabel(window)
    label_Name.setText("Hello, " + fName)
    label_Name.setFont(QFont("Roboto", 22))
    #grid.addWidget(label_Name,0,0)
    label_Name.move(20,10)

    #Card number: <---- ---- ---- ---->
    label_Card = QLabel(window)
    label_Card.setText("Card Number: " + cardNo)
    label_Card.setFont(QFont("Roboto", 13))
    label_Card.move(20,70)

    #Number of Rides
    label_RidesNo = QLabel(window)
    label_RidesNo.setText(noOfRides)
    label_RidesNo.setFont(QFont("Roboto", 34))
    label_RidesNo.move(120, 180)

    #Rides Label
    label_Rides = QLabel(window)
    label_Rides.setText("Number of Rides Left")
    label_Rides.setFont(QFont("Roboto", 12))
    label_Rides.move(40, 260)

    #Last Ride Date
    label_RidesNo = QLabel(window)
    label_RidesNo.setText(lastRide)
    label_RidesNo.setFont(QFont("Roboto", 24))
    label_RidesNo.move(310, 190)

    #Last Ride Label
    label_Rides = QLabel(window)
    label_Rides.setText("Last Ride")
    label_Rides.setFont(QFont("Roboto", 12))
    label_Rides.move(370, 260)

    #Last Recharge Date
    label_RidesNo = QLabel(window)
    label_RidesNo.setText(lastRide)
    label_RidesNo.setFont(QFont("Roboto", 24))
    label_RidesNo.move(590, 190)

    #Last Recharge Label
    label_Rides = QLabel(window)
    label_Rides.setText("Last Recharge")
    label_Rides.setFont(QFont("Roboto", 12))
    label_Rides.move(630, 260)

    #Edit Account Button
    button_editAc = QPushButton("Edit Account", window)
    button_editAc.setFont(QFont("Roboto", 10))
    button_editAc.setGeometry(40, 400, 200,50)

    #ERecharge Button
    button_Recharge = QPushButton("Recharge", window)
    button_Recharge.setFont(QFont("Roboto", 10))
    button_Recharge.setGeometry(310, 400, 200,50)

    #NFC Button
    button_NFC = QPushButton("NFC", window)
    button_NFC.setFont(QFont("Roboto", 10))
    button_NFC.setGeometry(590, 400, 200,50)


    window.show()
    app.exec_()

if __name__ == '__main__':
    main()