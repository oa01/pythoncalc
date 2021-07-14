
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
first_number = 0
second_number = 0
output = 0
choice = 0

#below are the functions








class Ui_MainWindow(object):

    def add(self):
        global first_number
        global second_number
        global output
        first_number = self.lineEdit.text()
        second_number = self.lineEdit_2.text()
        output = int(first_number) + int(second_number)
        self.lineEdit_3.setText(f"{output}")
        print(f"The Result is {output}")

    def multi(self):
        global first_number
        global second_number
        global output
        first_number = self.lineEdit.text()
        second_number = self.lineEdit_2.text()
        output = int(first_number) * int(second_number)
        self.lineEdit_3.setText(f"{output}")
        print(f"The Result is {output}")

    def div(self):
        global first_number
        global second_number
        global output
        if second_number == 0:
            print("You cant divide by 0")

        else:
            first_number = self.lineEdit.text()
            second_number = self.lineEdit_2.text()
            output = first_number / second_number
            self.lineEdit_3.setText(f"{output}")
            print(f"The Result is {output}")

    def sub(self):
        global first_number
        global second_number
        global output
        first_number = self.lineEdit.text()
        second_number = self.lineEdit_2.text()
        output = int(first_number) - int(second_number)
        self.lineEdit_3.setText(f"{output}")
        print(f"The Result is {output}")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 266, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 287, 56, 17))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 308, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 329, 56, 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 130, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 135, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 185, 41, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 180, 111, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 230, 41, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 230, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 350, 56, 17))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 18))
        self.menubar.setObjectName("menubar")
        self.menutaschenrechner = QtWidgets.QMenu(self.menubar)
        self.menutaschenrechner.setObjectName("menutaschenrechner")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menutaschenrechner.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.multi)
        self.pushButton_5.clicked.connect(self.div)
        self.pushButton_6.clicked.connect(self.sub)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "*"))
        self.pushButton_5.setText(_translate("MainWindow", "/"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_6.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "1. Zahl"))
        self.label_2.setText(_translate("MainWindow", "2. Zahl"))
        self.label_3.setText(_translate("MainWindow", "Ergebinis"))
        self.pushButton_3.setText(_translate("MainWindow", "calc"))
        self.menutaschenrechner.setTitle(_translate("MainWindow", "taschenrechner"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())









