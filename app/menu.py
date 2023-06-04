import sys
import subprocess
import webbrowser
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QFontDatabase, QPixmap
from start_parser import StartParserWindow
from dbase import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db = Database('app/spt_db.db')
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
        self.connections()

    def connections(self):
        self.UI.pushButton.clicked.connect(self.start_parser)
        self.UI.pushButton_2.clicked.connect(self.open_source)
        self.UI.radioButton.clicked.connect(self.change_theme)
        self.UI.pushButton_4.clicked.connect(self.terms)

    def start_parser(self):
        if not self.db.check_terms() == None:
            if self.db.check_terms()[0] == 'agree':
                self.parser = StartParserWindow(self)
                self.parser.show()
            else:
                self.terms()
        else:
            self.terms()

    def open_source(self):
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
        self.terms_popup.setIconPixmap(QPixmap('app/logo.png'))
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
    QFontDatabase.addApplicationFont('app/fonts/Rubik-Italic.ttf')
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
