# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adm_livro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cad_livro = QtWidgets.QPushButton(self.centralwidget)
        self.cad_livro.setGeometry(QtCore.QRect(110, 240, 131, 51))
        self.cad_livro.setObjectName("cad_livro")
        self.remove_livro = QtWidgets.QPushButton(self.centralwidget)
        self.remove_livro.setGeometry(QtCore.QRect(590, 240, 131, 51))
        self.remove_livro.setObjectName("remove_livro")
        self.tela_adm_user = QtWidgets.QLabel(self.centralwidget)
        self.tela_adm_user.setGeometry(QtCore.QRect(250, 20, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tela_adm_user.setFont(font)
        self.tela_adm_user.setObjectName("tela_adm_user")
        self.edit_livro = QtWidgets.QPushButton(self.centralwidget)
        self.edit_livro.setGeometry(QtCore.QRect(430, 240, 131, 51))
        self.edit_livro.setObjectName("edit_livro")
        self.list_livro = QtWidgets.QPushButton(self.centralwidget)
        self.list_livro.setGeometry(QtCore.QRect(270, 240, 131, 51))
        self.list_livro.setObjectName("list_livro")
        self.voltar = QtWidgets.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(590, 480, 151, 61))
        self.voltar.setObjectName("voltar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cad_livro.setText(_translate("MainWindow", "Cadastrar Livro"))
        self.remove_livro.setText(_translate("MainWindow", "Remover Livro"))
        self.tela_adm_user.setText(_translate("MainWindow", "ADMINISTRAÇÃO DE LIVRO"))
        self.edit_livro.setText(_translate("MainWindow", "Editar Livro"))
        self.list_livro.setText(_translate("MainWindow", "Listar Livros"))
        self.voltar.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
