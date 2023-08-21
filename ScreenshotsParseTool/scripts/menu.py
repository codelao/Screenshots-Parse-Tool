import sys
import subprocess
import webbrowser
import setproctitle
from ScreenshotsParseTool import NAME, VERSION, PATH
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QFontDatabase, QPixmap
from .startparser import StartParserWindow
from .ui_menu import Ui_MainWindow
from .dbase import Database
from .check_internet import check_internet_connection


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db = Database(PATH + '/database/spt_db.db')
        self.theme = self.db.check_theme()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        if self.theme == None or self.theme[0] == 'light':
            self.setStyleSheet('QMainWindow {\n'
            'background-color: #FFFFFF;\n'
            '}')
        else:
            self.setStyleSheet('QMainWindow {\n'
            'background-color: #330230;\n'
            '}')
        QFontDatabase.addApplicationFont(PATH + '/fonts/Rubik.ttf')
        self.connections()

    def connections(self):
        self.UI.button1.clicked.connect(self.start_parser)
        self.UI.button2.clicked.connect(self.stats)
        self.UI.OpenREADME.triggered.connect(self.readme)
        self.UI.TermsofUse.triggered.connect(self.terms)
        self.UI.ThemeLight.triggered.connect(self.change_theme)
        self.UI.ThemeDark.triggered.connect(self.change_theme)

    def start_parser(self):
        if not self.db.check_terms() == None:
            if check_internet_connection() == True:
                self.parser = StartParserWindow(self)
                self.parser.show()
            else:
                self.internet_error_popup = QMessageBox(self)
                self.internet_error_popup.setWindowTitle('Internet error')
                self.internet_error_popup.setIconPixmap(QPixmap(PATH + '/images/logo.png'))
                self.internet_error_popup.setStyleSheet('QMessageBox {\n'
                                                        'background-color: #FFFFFF;\n'
                                                        'color: #000000;\n'
                                                        '}')
                self.internet_error_popup.move(400, 300)
                self.internet_error_popup.setIcon(QMessageBox.Icon.Warning)
                self.internet_error_popup.setText('Check your internet connection or try again.')
                self.okButton = self.internet_error_popup.addButton(QMessageBox.StandardButton.Ok)
                self.internet_error_popup.setDefaultButton(self.okButton)
                self.internet_error_popup.exec()
        else:
            self.terms()

    def stats(self):
        self.count = self.db.get_screens_count()
        self.date = self.db.get_last_parse_date()
        if not self.count == None:
            self.stats_popup = QMessageBox(self)
            self.stats_popup.setWindowTitle('Statistics')
            self.stats_popup.setIconPixmap(QPixmap(PATH + '/images/logo.png'))
            self.stats_popup.setStyleSheet('QMessageBox {\n'
                                            'background-color: #FFFFFF;\n'
                                            'color: #000000;\n'
                                            '}')
            self.stats_popup.move(400, 300)
            self.stats_popup.setIcon(QMessageBox.Icon.Information)
            self.stats_popup.setText('Screenshots parsed: ' + str(self.count[0]) + '\nLast parse: ' + self.date[0])
            self.okButton = self.stats_popup.addButton(QMessageBox.StandardButton.Ok)
            self.stats_popup.setDefaultButton(self.okButton)
            self.stats_popup.exec()
        else:
            self.stats_popup = QMessageBox(self)
            self.stats_popup.setWindowTitle('Statistics')
            self.stats_popup.setIconPixmap(QPixmap(PATH + '/images/logo.png'))
            self.stats_popup.setStyleSheet('QMessageBox {\n'
                                            'background-color: #FFFFFF;\n'
                                            'color: #000000;\n'
                                            '}')
            self.stats_popup.move(400, 300)
            self.stats_popup.setIcon(QMessageBox.Icon.Information)
            self.stats_popup.setText('No data yet.')
            self.okButton = self.stats_popup.addButton(QMessageBox.StandardButton.Ok)
            self.stats_popup.setDefaultButton(self.okButton)
            self.stats_popup.exec()

    def readme(self):
        webbrowser.open('https://github.com/codelao/Screenshots-Parse-Tool/blob/main/README.md')

    def change_theme(self):
        sender = self.sender()
        if not self.theme == None:
            if self.theme[0] == 'light':
                if not sender == self.UI.ThemeLight:
                    self.db.update_theme(theme='dark')
                    QApplication.exit(0)
                    subprocess.Popen([sys.executable] + sys.argv)
                else:
                    pass
            else:
                if not sender == self.UI.ThemeDark:
                    self.db.update_theme(theme='light')
                    QApplication.exit(0)
                    subprocess.Popen([sys.executable] + sys.argv)
                else:
                    pass
        else:
            if not sender == self.UI.ThemeLight:
                self.db.add_theme(theme='dark')
                QApplication.exit(0)
                subprocess.Popen([sys.executable] + sys.argv)
            else:
                self.db.add_theme(theme='light')

    def terms(self):
        self.terms_popup = QMessageBox(self)
        self.terms_popup.setWindowTitle('Terms of Use')
        self.terms_popup.setIconPixmap(QPixmap(PATH + '/images/logo.png'))
        self.terms_popup.setStyleSheet('QMessageBox {\n'
                                        'background-color: #FFFFFF;\n'
                                        'color: #000000;\n'
                                        '}')
        self.terms_popup.move(400, 300)
        self.terms_popup.setIcon(QMessageBox.Icon.Warning)
        self.terms_popup.setText('DISCLAIMER\n\nIt is forbidden to use this tool for illegal or malicious purposes.\nDeveloper (Lao) is not responsible for the unethical use of this tool by other users.')
        self.terms_popup.setDetailedText('Screenshots Parse Tool\nLicensed under MIT')
        self.agreeButton = self.terms_popup.addButton('Agree', QMessageBox.ButtonRole.AcceptRole)
        self.terms_popup.addButton(QMessageBox.StandardButton.Cancel)
        self.terms_popup.setDefaultButton(self.agreeButton)
        self.terms_popup.exec()
        if self.terms_popup.clickedButton() == self.agreeButton:
            if self.db.check_terms() == None:
                self.db.add_terms(terms='agree')


def entry_point():
    app = QApplication(sys.argv)
    app.setApplicationName(NAME)
    app.setApplicationVersion(VERSION)
    setproctitle.setproctitle(NAME)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    entry_point()
