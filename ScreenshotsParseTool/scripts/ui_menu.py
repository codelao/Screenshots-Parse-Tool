import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.current_dir = os.path.dirname(__file__)
        self.path = os.path.abspath(os.path.join(self.current_dir, os.pardir))
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(430, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path + "/images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 126))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.text.setFont(font)
        self.text.setStyleSheet("QLabel {\n"
"    color: #73036B;\n"
"}")
        self.text.setText("Screenshots Parse Tool")
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.button1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.button1.setFont(font)
        self.button1.setToolTip("Start parsing screenshots")
        self.button1.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: #73036B; \n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.button1.setText("Launch")
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.button2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        self.button2.setFont(font)
        self.button2.setToolTip("Show your statistics")
        self.button2.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: #73036B; \n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #050359;\n"
"}")
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.image = QtWidgets.QLabel(parent=self.centralwidget)
        self.image.setGeometry(QtCore.QRect(150, 40, 291, 301))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(self.path + "/images/logo.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 430, 37))
        self.menuBar.setObjectName("menuBar")
        self.Theme = QtWidgets.QMenu(parent=self.menuBar)
        self.Theme.setObjectName("Theme")
        self.Help = QtWidgets.QMenu(parent=self.menuBar)
        self.Help.setObjectName("Help")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDark = QtGui.QAction(parent=MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtGui.QAction(parent=MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.ThemeDark = QtGui.QAction(parent=MainWindow)
        self.ThemeDark.setObjectName("ThemeDark")
        self.ThemeLight = QtGui.QAction(parent=MainWindow)
        self.ThemeLight.setObjectName("ThemeLight")
        self.OpenREADME = QtGui.QAction(parent=MainWindow)
        self.OpenREADME.setObjectName("OpenREADME")
        self.TermsofUse = QtGui.QAction(parent=MainWindow)
        self.TermsofUse.setObjectName("TermsofUse")
        self.Theme.addAction(self.ThemeDark)
        self.Theme.addAction(self.ThemeLight)
        self.Help.addAction(self.OpenREADME)
        self.Help.addAction(self.TermsofUse)
        self.menuBar.addAction(self.Theme.menuAction())
        self.menuBar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screenshots Parse Tool"))
        self.button2.setText(_translate("MainWindow", "Statistics"))
        self.Theme.setTitle(_translate("MainWindow", "Theme"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.ThemeDark.setText(_translate("MainWindow", "Dark"))
        self.ThemeLight.setText(_translate("MainWindow", "Light"))
        self.OpenREADME.setText(_translate("MainWindow", "Open README"))
        self.TermsofUse.setText(_translate("MainWindow", "Terms of Use"))
