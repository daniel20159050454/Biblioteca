import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
import sys
from Telas_Usuario.tela_de_login import Ui_Tela_Login
from Telas_Usuario.adm_livro import Ui_MainWindow as Ui_Adm_Livro
import os
from PyQt5.QtCore import pyqtSlot


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(800, 600)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.adm_livro = Ui_Adm_Livro()
        self.adm_livro.setupUi(self.stack1)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)


class Main(QMainWindow, Ui_Main):
    def _init_(self, parent=None):
        super(Main, self)._init_(parent)
        self.setupUi(self)

        self.tela_login.entrar.clicked.connect(self.adm_livro)

    def adm_livro(self):
        self.self.QtStack.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())