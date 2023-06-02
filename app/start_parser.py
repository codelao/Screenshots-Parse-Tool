from PyQt6.QtWidgets import QDialog, QApplication
from dbase import Database
from get_screenshot import downloader


class StartParserWindow(QDialog):
    def __init__(self, parent):
        super(StartParserWindow, self).__init__()
        self.db = Database('app/spt_db.db')
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
        self.UI.progressBar.setValue(0)

    def back(self):
        self.hide()
        self.parent.show()
