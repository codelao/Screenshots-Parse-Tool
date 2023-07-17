import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.current_dir = os.path.dirname(__file__)
        self.path = os.path.abspath(os.path.join(self.current_dir, os.pardir))
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(280, 200)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path + "/images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(15)
        self.text.setFont(font)
        self.text.setToolTip("")
        self.text.setStyleSheet("color: #73036B;")
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.spinBox = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        self.spinBox.setFont(font)
        self.spinBox.setToolTip("Select the number of screenshots need to be parsed")
        self.spinBox.setStyleSheet("QSpinBox {\n"
"    background-color: #73036B;\n"
"    color: white;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.button1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        self.button1.setFont(font)
        self.button1.setToolTip("Start parsing screenshots")
        self.button1.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #73036B; \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.button2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.button2.setMinimumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        self.button2.setFont(font)
        self.button2.setToolTip("Go back to menu")
        self.button2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #73036B; \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.progressBar = QtWidgets.QProgressBar(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        self.progressBar.setFont(font)
        self.progressBar.setToolTip("")
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border-radius: 0px;\n"
"    background-color: #D4D4D4;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #050359;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Screenshots Parse Tool"))
        self.text.setText(_translate("Dialog", "Number of screenshots:"))
        self.button1.setText(_translate("Dialog", "Launch"))
        self.button2.setText(_translate("Dialog", "Back"))
