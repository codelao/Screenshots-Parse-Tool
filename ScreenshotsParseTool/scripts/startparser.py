import datetime
from ScreenshotsParseTool import __path__
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt6.QtGui import QPixmap, QFontDatabase
from .dbase import Database
from .ui_startparser import Ui_Dialog
from .get_screenshot import downloader


class StartParserWindow(QDialog):
    def __init__(self, parent):
        super(StartParserWindow, self).__init__()
        self.db = Database(__path__ + '/database/spt_db.db')
        self.theme = self.db.check_theme()
        self.UI = Ui_Dialog()
        self.UI.setupUi(self)
        if self.theme == None or self.theme[0] == 'light':
            self.setStyleSheet('QDialog {\n'
            'background-color: #FFFFFF;\n'
            '}')
        else:
            self.setStyleSheet('QDialog {\n'
            'background-color: #330230;\n'
            '}')
        QFontDatabase.addApplicationFont(__path__ + '/fonts/Rubik.ttf')
        self.connections()
        self.parent = parent

    def connections(self):
        self.UI.button1.clicked.connect(self.launch)
        self.UI.button2.clicked.connect(self.back)

    def launch(self):
        self.screens_count = self.UI.spinBox.value()
        self.UI.progressBar.setMinimum(0)
        self.UI.progressBar.setMaximum(self.screens_count)
        self.UI.button1.setEnabled(False)
        self.UI.button2.setEnabled(False)
        self.UI.spinBox.setEnabled(False)
        for screens in range(self.screens_count):
            downloader()
            self.UI.progressBar.setValue(screens + 1)
            QApplication.processEvents()
        self.finish_popup = QMessageBox(self)
        self.finish_popup.setWindowTitle('Parsing finished')
        self.finish_popup.setIconPixmap(QPixmap(__path__ + '/images/logo.png'))
        self.finish_popup.setStyleSheet('QMessageBox {\n'
                                        'background-color: #FFFFFF;\n'
                                        'color: #000000;\n'
                                        '}')
        self.finish_popup.move(400, 300)
        self.finish_popup.setIcon(QMessageBox.Icon.Information)
        self.finish_popup.setText('Screenshots (' + str(self.screens_count) + ') successfully parsed!')
        self.okButton = self.finish_popup.addButton(QMessageBox.StandardButton.Ok)
        self.finish_popup.setDefaultButton(self.okButton)
        self.finish_popup.exec()
        if self.finish_popup.clickedButton() == self.okButton:
            self.count = self.db.get_screens_count()
            self.today = datetime.datetime.today()
            self.date = self.today.strftime("%m/%d/%Y")
            if not self.count == None:
                self.screens = self.screens_count + self.count[0]
                self.db.update_stats(screens=self.screens, last_parse=self.date)
            else:
                self.db.add_stats(screens=self.screens_count, last_parse=self.date)
        self.UI.button1.setEnabled(True)
        self.UI.button2.setEnabled(True)
        self.UI.spinBox.setEnabled(True)
        self.UI.progressBar.setValue(0)

    def back(self):
        self.hide()
        self.parent.show()
