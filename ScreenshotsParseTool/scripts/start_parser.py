import os
import datetime
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt6.QtGui import QPixmap
from dbase import Database
from get_screenshot import downloader


class StartParserWindow(QDialog):
    def __init__(self, parent):
        super(StartParserWindow, self).__init__()
        self.current_dir = os.path.dirname(__file__)
        self.path = os.path.abspath(os.path.join(self.current_dir, os.pardir))
        self.db = Database(self.path + '/database/spt_db.db')
        self.theme = self.db.check_theme()
        if not self.theme == None:
            if self.theme[0] == 'light':
                from start_light import Ui_Dialog
                self.UI = Ui_Dialog()
                self.UI.setupUi(self)
            else:
                from start_dark import Ui_Dialog
                self.UI = Ui_Dialog()
                self.UI.setupUi(self)
        else:
            from start_light import Ui_Dialog
            self.UI = Ui_Dialog()
            self.UI.setupUi(self)
        self.connections()
        self.parent = parent

    def connections(self):
        self.UI.pushButton.clicked.connect(self.run)
        self.UI.pushButton_2.clicked.connect(self.back)

    def run(self):
        self.screens_count = self.UI.spinBox.value()
        self.UI.progressBar.setMinimum(0)
        self.UI.progressBar.setMaximum(self.screens_count)
        for screens in range(self.screens_count):
            downloader()
            self.UI.progressBar.setValue(screens + 1)
            QApplication.processEvents()
        self.finish_popup = QMessageBox(self)
        self.finish_popup.setWindowTitle('Parsing finished')
        self.finish_popup.setIconPixmap(QPixmap(self.path + '/images/logo.png'))
        self.finish_popup.move(400, 300)
        self.finish_popup.setIcon(QMessageBox.Icon.Information)
        self.finish_popup.setText('Screenshots (' + str(self.screens_count) + ') successfully parsed!')
        self.okButton = self.finish_popup.setDefaultButton(QMessageBox.StandardButton.Ok)
        self.finish_popup.exec()
        if self.finish_popup.clickedButton() == self.okButton:
            self.count = self.db.get_screens_count()[0]
            self.today = datetime.datetime.today()
            self.date = self.today.strftime("%m/%d/%Y")
            if not self.count == None:
                self.screens = self.screens_count + self.count
                self.db.update_stats(screens=self.screens, last_parse=self.date)
            else:
                self.db.add_stats(screens=self.screens_count, last_parse=self.date)
        self.UI.progressBar.setValue(0)

    def back(self):
        self.hide()
        self.parent.show()
