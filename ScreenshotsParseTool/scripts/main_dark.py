import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.current_dir = os.path.dirname(__file__)
        self.path = os.path.abspath(os.path.join(self.current_dir, os.pardir))
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(450, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path + "/images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #333333;\n"
"}")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label.setText("Screenshots Parse Tool")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: grey;\n"
"}")
        self.label_2.setText("v0.10.5")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setToolTip("")
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #73036B;    \n"
"    border-radius: 10px;\n"
"    border-width: 3px;\n"
"    border-style: outset;\n"
"    border-color: #8B8B8B;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.pushButton.setText("Start parser")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 280, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #73036B;    \n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.pushButton_2.setText("Statistics")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 310, 201, 201))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(self.path + "/images/logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 710, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(15)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: grey;\n"
"}")
        self.label_4.setText("by Lao")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 600, 451, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(self.path + "/images/rectangle.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(160, 610, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        font.setItalic(True)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("QRadioButton {\n"
"    color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-radius: 8px;\n"
"}\n"
"        \n"
"QRadioButton::indicator:checked {\n"
"    background-color: black;\n"
"}\n"
"        \n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: white;\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 660, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(18)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setToolTip("")
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #050359;    \n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #73036B;\n"
"}")
        self.pushButton_4.setText("Terms of use")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.radioButton.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPT"))
        self.radioButton.setText(_translate("MainWindow", " Light theme"))
