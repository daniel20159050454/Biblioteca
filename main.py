import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
import sys
from Telas_Usuario.tela_de_login import Ui_Tela_Login
from Telas_Usuario.adm_livro import Ui_MainWindow as Ui_Adm_Livro
from Telas_Usuario.cad_livro import Ui_MainWindow as Ui_Cadastro_Livro
from Telas_Usuario.editar_livro import Ui_MainWindow as Ui_Editar_Livro
from Telas_Usuario.listar_livro import Ui_MainWindow as Ui_Listar_Livro
from Telas_Usuario.remover_livro import Ui_MainWindow as Ui_Remover_Livro
import os
from PyQt5.QtCore import pyqtSlot
from firebase import firebase


firebaseConfig = {
            'apiKey': "AIzaSyD6NeWtwGK0yeDfG6C1W-ZesVnjNFlVnSw",
            'authDomain': "biblioteca-b2317.firebaseapp.com",
            'databaseURL': "https://biblioteca-b2317.firebaseio.com",
            'projectId': "biblioteca-b2317",
            'storageBucket': "",
            'messagingSenderId': "1080656799035",
            'appId': "1:1080656799035:web:0064e0d7e84c5e7d"}

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(800, 600)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.adm_livro = Ui_Adm_Livro()
        self.adm_livro.setupUi(self.stack1)

        self.cadastro_livro = Ui_Cadastro_Livro()
        self.cadastro_livro.setupUi(self.stack2)

        self.listar_livroo = Ui_Listar_Livro()
        self.listar_livroo.setupUi(self.stack3)

        self.editar_livroo = Ui_Editar_Livro()
        self.editar_livroo.setupUi(self.stack4)

        self.remover_livroo = Ui_Remover_Livro()
        self.remover_livroo.setupUi(self.stack5)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self._firebase = firebase(firebaseConfig)

        self.tela_login.entrar.clicked.connect(self.admnistracao_livro)
        self.adm_livro.cad_livro.clicked.connect(self.cadast_livro)
        self.adm_livro.list_livro.clicked.connect(self.listar_livros)
        self.adm_livro.edit_livro.clicked.connect(self.edit_livro)
        self.adm_livro.remove_livro.clicked.connect(self.deletar_livro)
        
        self.adm_livro.voltar.clicked.connect(self.voltar_P_login)
        self.cadastro_livro.voltar.clicked.connect(self.voltar_P_telaAdm)
        self.listar_livroo.voltar.clicked.connect(self.voltar_P_telaAdm)
        self.editar_livroo.voltar.clicked.connect(self.voltar_P_telaAdm)
        self.remover_livroo.voltar.clicked.connect(self.voltar_P_telaAdm)

        self.cadastro_livro.salvar_livro.clicked.connect(self.cadastrando_livro)
        self.remover_livroo.bottonBisbn_2.clicked.connect(self.apagar)
        #self.remover_livroo.excluir_livro.clicked.connect(self.apagar)
        self.listar_livroo.bottonBisbn.clicked.connect(self.buscar)

    def admnistracao_livro(self):
        '''if self.tela_login.email_login.text() == '' or self.tela_login.senha.text() == '':
            return QMessageBox.about(self, 'Atenção', 'Desculpe, campos invalidos!')
        else:'''
        self.QtStack.setCurrentIndex(1)

    def cadast_livro(self):
        self.QtStack.setCurrentIndex(2)

    def listar_livros(self):
        self.QtStack.setCurrentIndex(3)

    def edit_livro(self):
        self.QtStack.setCurrentIndex(4)

    def deletar_livro(self):
        self.QtStack.setCurrentIndex(5)

    def voltar_P_login(self):
        self.QtStack.setCurrentIndex(0)

    def voltar_P_telaAdm(self):
        self.QtStack.setCurrentIndex(1)

    def cadastrando_livro(self):
        livro = {
            'titulo': self.cadastro_livro.title.text(),
            'autor' : self.cadastro_livro.autor.text(),
            'isbn' : self.cadastro_livro.isbn.text(),
            'editora' : self.cadastro_livro.editora.text(),
        }
        self._firebase.addLivro(livro)
        self.QtStack.setCurrentIndex(1)
    
    def apagar(self):
        result = self.remover_livroo.BuscaISBN_2.text()
        self._firebase.remover_Livro(result)
        self.QtStack.setCurrentIndex(1)

    def buscar(self):
        isbn = self.listar_livroo.BuscaISBN.text()
        if isbn == self._firebase.buscaFirebase()
        
        self.listar_livroo.result_buscaLivro.setText('adasd')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())