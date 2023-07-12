import sys
import os
import subprocess
import webbrowser
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenuBar, QMenu
from PyQt6.QtGui import QFontDatabase, QPixmap, QAction
from start_parser import StartParserWindow
from dbase import Database
from check_internet import check_internet_connection


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.current_dir = os.path.dirname(__file__)
        self.path = os.path.abspath(os.path.join(self.current_dir, os.pardir))
        self.db = Database(self.path + '/database/spt_db.db')
        self.theme = self.db.check_theme()
        if not self.theme == None:
            if self.theme[0] == 'light':
                from main_light import Ui_MainWindow
                self.UI = Ui_MainWindow()
                self.UI.setupUi(self)
            else:
                from main_dark import Ui_MainWindow
                self.UI = Ui_MainWindow()
                self.UI.setupUi(self)
        else:
            from main_light import Ui_MainWindow
            self.UI = Ui_MainWindow()
            self.UI.setupUi(self)
        QFontDatabase.addApplicationFont(self.path + '/fonts/Rubik.ttf')
        self.menu_bar = QMenuBar(self)
        self.info = QMenu('SPT', self)
        self.menu_bar.addMenu(self.info)
        self.open_source = QAction('Open source', self)
        self.info.addAction(self.open_source)
        self.setMenuBar(self.menu_bar)
        self.connections()

    def connections(self):
        self.UI.pushButton.clicked.connect(self.start_parser)
        self.UI.pushButton_2.clicked.connect(self.stats)
        self.UI.radioButton.clicked.connect(self.change_theme)
        self.UI.pushButton_4.clicked.connect(self.terms)
        self.open_source.triggered.connect(self.open_repository)

    def start_parser(self):
        if not self.db.check_terms() == None:
            if self.db.check_terms()[0] == 'agree':
                if check_internet_connection() == True:
                    self.parser = StartParserWindow(self)
                    self.parser.show()
                else:
                    self.internet_error_popup = QMessageBox(self)
                    self.internet_error_popup.setWindowTitle('Internet error')
                    self.internet_error_popup.setIconPixmap(QPixmap(self.path + '/images/logo.png'))
                    self.internet_error_popup.move(400, 300)
                    self.internet_error_popup.setIcon(QMessageBox.Icon.Warning)
                    self.internet_error_popup.setText('Check your internet connection or disable VPN.')
                    self.internet_error_popup.setDefaultButton(QMessageBox.StandardButton.Ok)
                    self.internet_error_popup.exec()
            else:
                self.terms()
        else:
            self.terms()

    def stats(self):
        self.count = self.db.get_screens_count()[0]
        self.date = self.db.get_last_parse_date()[0]
        if not self.count == None:
            self.stats_popup = QMessageBox(self)
            self.stats_popup.setWindowTitle('Statistics')
            self.stats_popup.setIconPixmap(QPixmap(self.path + '/images/logo.png'))
            self.stats_popup.move(400, 300)
            self.stats_popup.setIcon(QMessageBox.Icon.Information)
            self.stats_popup.setText('Screenshots parsed: ' + str(self.count) + '\nLast parse: ' + self.date)
            self.stats_popup.setDefaultButton(QMessageBox.StandardButton.Ok)
            self.stats_popup.exec()
        else:
            self.stats_popup = QMessageBox(self)
            self.stats_popup.setWindowTitle('Statistics')
            self.stats_popup.setIconPixmap(QPixmap(self.path + '/images/logo.png'))
            self.stats_popup.move(400, 300)
            self.stats_popup.setIcon(QMessageBox.Icon.Information)
            self.stats_popup.setText('No data yet.')
            self.stats_popup.setDefaultButton(QMessageBox.StandardButton.Ok)
            self.stats_popup.exec()

    def open_repository(self):
        webbrowser.open('https://github.com/codelao/Screenshots-Parse-Tool')

    def change_theme(self):
        if not self.theme == None:
            if self.theme[0] == 'light':
                self.db.update_theme(theme='dark')
                QApplication.exit(0)
                subprocess.Popen([sys.executable] + sys.argv)
            else:
                self.db.update_theme(theme='light')
                QApplication.exit(0)
                subprocess.Popen([sys.executable] + sys.argv)
        else:
            self.db.add_theme(theme='dark')
            QApplication.exit(0)
            subprocess.Popen([sys.executable] + sys.argv)

    def terms(self):
        self.terms_popup = QMessageBox(self)
        self.terms_popup.setWindowTitle('Terms of use')
        self.terms_popup.setIconPixmap(QPixmap(self.path + '/images/logo.png'))
        self.terms_popup.move(400, 300)
        self.terms_popup.setIcon(QMessageBox.Icon.Warning)
        self.terms_popup.setText('DISCLAIMER')
        self.terms_popup.setDetailedText('It is forbidden to use this tool for illegal or malicious purposes.\nDeveloper (Lao) is not responsible for the unethical use of this tool by other users.\n\nScreenshots Parse Tool\nv0.8.5\nLicensed under MIT')
        self.agreeButton = self.terms_popup.addButton("Agree", QMessageBox.ButtonRole.ActionRole)
        self.terms_popup.setDefaultButton(self.agreeButton)
        self.terms_popup.exec()
        if self.terms_popup.clickedButton() == self.agreeButton:
            if not self.db.check_terms() == None:
                pass
            else:
                self.db.add_terms(terms='agree')
                             

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
