from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(320, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: white;\n"
"}")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #050359;\n"
"}")
        self.label.setText("Select number of screenshots:")
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(parent=Dialog)
        self.spinBox.setGeometry(QtCore.QRect(130, 70, 61, 31))
        self.spinBox.setStyleSheet("QSpinBox {\n"
"    background-color: #73036B;\n"
"    color: white;\n"
"}\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 161, 31))
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
"}\n"
"QPushButton:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.pushButton.setText("Run")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 170, 121, 31))
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
        self.pushButton_2.setText("Back")
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(parent=Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 210, 301, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border-radius: 0px;\n"
"    background-color: #D4D4D4;\n"
"    text-align: center;\n"
"    color: #73036B;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #050359;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SPT -> Start parser"))
