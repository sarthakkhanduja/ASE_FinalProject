from cProfile import label
from curses import window
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
def main():
    #Global variables
    fName = "Sarthak Khanduja"
    cardNo = "4456 0211 6458 9899"

    #Main App and Window
    app = QApplication([])
    window = QWidget()
    window.setGeometry(200,200,1300,700)

    #Hello, <name>
    label_Name = QLabel(window)
    label_Name.setText("Hello, " + fName)
    label_Name.setFont(QFont("Roboto", 22))
    label_Name.move(20,10)

    #Card number: <---- ---- ---- ---->
    label_Card = QLabel(window)
    label_Card.setText("Card Number: " + cardNo)
    label_Card.setFont(QFont("Roboto", 14))
    #label_Card.move(20,60)
    label_Card.setAlignment()

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()